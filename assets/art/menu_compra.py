import shutil

import WConio2 as W

from assets.art.base import escrever
from configs.config import ENTER

SETA_CIMA = 72          # códigos do WConio2.getch() (se preferir, mova estes dois para o config.py)
SETA_BAIXO = 80

# letras que escolhem os itens à venda (aparecem na borda de baixo de cada caixa).
# Troque as letras como quiser: só não pode repetir nem usar W/S (são das setas dos botões).
TECLAS_COMPRA = {
    "item":    ["q", "e"],      # letra do item 1 e do item 2
    "voucher": ["r"],           # letra do voucher
    "pacote":  ["f", "g"],      # letra do pacote 1 e do pacote 2
}


def _validar_teclas(mapa):
    """Confere TECLAS_COMPRA e devolve {letra: (acao, indice)} para consulta rápida."""
    quantidade = {"item": 2, "voucher": 1, "pacote": 2}
    for acao, n in quantidade.items():
        if len(mapa.get(acao, [])) != n:
            raise ValueError(f"TECLAS_COMPRA: '{acao}' precisa de {n} letra(s)")
    letras = [l.lower() for lista in mapa.values() for l in lista]
    if any(len(l) != 1 or not l.isalpha() for l in letras):
        raise ValueError("TECLAS_COMPRA: use uma letra por opção")
    if len(set(letras)) != len(letras):
        raise ValueError("TECLAS_COMPRA: tem letra repetida")
    if {"w", "s"} & set(letras):
        raise ValueError("TECLAS_COMPRA: W e S são das setas (Próxima Rodada / Reroll)")
    return {l.lower(): (acao, i) for acao, lista in mapa.items() for i, l in enumerate(lista)}


LETRA_PARA_ACAO = _validar_teclas(TECLAS_COMPRA)

ESPACO = 1              # espaço entre os dois botões empilhados (linhas)
ESCALA_ALTURA = 0.58    # fatia da altura livre que a loja ocupa (o resto, em cima, fica para os coringas)
ESCALA_LARGURA = 0.67   # fatia da largura livre que a loja ocupa (no original, ~2/3 da área ao lado do menu)
ESCALA_CARTA = 0.6      # fatia da coluna ("slot") que cada caixa ocupa; o resto vira espaço entre as caixas
FATIA_FILEIRA1 = 0.64   # parte da altura da loja que fica na fileira de cima (itens); o resto é voucher/pacotes
MIN_CARTA = 16          # menor largura de uma caixa
MIN_FOLGA = 2           # menor espaço entre duas caixas (colunas)
MIN_LARGURA = 3 * (MIN_CARTA + MIN_FOLGA) + 4   # menor largura (colunas) em que a loja cabe
MIN_ALTURA = 18         # menor altura (linhas) em que a loja cabe

# dados de exemplo: troque pelos itens reais sorteados a cada visita
LOJA_EXEMPLO = {
    "reroll": 5,
    "itens": [
        {"nome": "Joker", "tipo": "Coringa", "preco": 4},
        {"nome": "Mercúrio", "tipo": "Planeta", "preco": 3},
    ],
    "voucher": {"nome": "Excedente", "tipo": "Voucher", "preco": 10},
    "pacotes": [
        {"nome": "Pacote Coringa", "tipo": "Pacote", "preco": 4},
        {"nome": "Pacote Arcano", "tipo": "Pacote", "preco": 4},
    ],
}

# "selecionado" (só os botões são selecionáveis): 0 = Próxima Rodada, 1 = Reroll
# o resto é escolhido apertando a letra mostrada na borda de baixo da caixa (TECLAS_COMPRA)


def caixa(x, y, w, h, linhas, cor=W.WHITE, preco=None, selecionado=False, tecla=None):
    """Desenha uma caixa w x h em (x, y) com as linhas de texto centralizadas.
    Se tiver preco, ele aparece no meio da borda de cima; se tiver tecla, no meio da de baixo.
    Selecionada = fundo claro."""
    interno = w - 2
    if len(linhas) > h - 2:                 # caixa baixa demais: junta o texto numa linha só
        linhas = [" ".join(linhas)]
    topo = "─" * interno
    if preco is not None:
        topo = f" ${preco} ".center(interno, "─")

    W.textbackground(W.BLACK)
    W.textcolor(cor)
    W.gotoxy(x, y)
    escrever("┌" + topo + "┐")

    comeco = (h - 2 - len(linhas)) // 2         # linha onde o texto começa (centraliza na vertical)
    for i in range(h - 2):
        k = i - comeco
        texto = linhas[k][:interno] if 0 <= k < len(linhas) else ""
        W.gotoxy(x, y + 1 + i)
        W.textbackground(W.BLACK)
        W.textcolor(cor)
        escrever("│")
        if selecionado:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(interno))
        W.textbackground(W.BLACK)
        W.textcolor(cor)
        escrever("│")

    W.gotoxy(x, y + h - 1)
    base = "─" * interno
    if tecla is not None:
        base = f" [{tecla}] ".center(interno, "─")
    escrever("└" + base + "┘")
    W.textbackground(W.BLACK)
    W.textcolor(W.LIGHTGRAY)


def moldura(x, y, w, h):
    """Moldura dupla da loja (limpa o interior com espaços)."""
    W.textbackground(W.BLACK)
    W.textcolor(W.LIGHTGRAY)
    W.gotoxy(x, y)
    escrever("╔" + "═" * (w - 2) + "╗")
    for i in range(1, h - 1):
        W.gotoxy(x, y + i)
        escrever("║" + " " * (w - 2) + "║")
    W.gotoxy(x, y + h - 1)
    escrever("╚" + "═" * (w - 2) + "╝")


def desenhar_loja(estado, x, y=2, loja=LOJA_EXEMPLO, selecionado=0):
    """Desenha SÓ o painel da loja (sem menu lateral), encostado embaixo e centralizado na área livre.
    O tamanho vem do tamanho do terminal (o painel é baixo e largo; os botões são mais largos que as cartas).
    x = primeira coluna livre, logo depois do seu menu lateral (a loja se centraliza sozinha dali pra frente).
    Devolve False (e pede para aumentar a janela) se o terminal for pequeno demais."""
    cols, linhas = shutil.get_terminal_size()      # lê o tamanho NA HORA (a janela pode ter mudado)

    w = cols - 2 - x            # largura livre (sem encostar na borda direita)
    h = linhas - 1 - y          # altura livre (sem encostar na borda de baixo)

    if w < MIN_LARGURA or h < MIN_ALTURA:
        W.gotoxy(x, y)
        escrever("Aumente a janela do terminal.".ljust(max(w, 0)))
        return False

    # --- altura: a loja ocupa uma fatia da altura livre, encostada embaixo ---
    ph = min(h, max(MIN_ALTURA, int(h * ESCALA_ALTURA)))
    y_painel = y + h - ph
    gap_v = max(2, ph // 12)                        # espaço entre as duas fileiras
    util = ph - 4 - gap_v                           # -4 = moldura + 1 linha de folga em cima e embaixo
    h1 = max(7, min(round(util * FATIA_FILEIRA1), util - 5))   # fileira de cima (itens); a de baixo fica com pelo menos 5
    h2 = util - h1                                  # fileira de baixo (voucher e pacotes)

    # --- largura: o painel é largo; cartas ocupam parte do slot e os botões quase o slot inteiro ---
    pw = min(w, max(MIN_LARGURA, int(w * ESCALA_LARGURA)))
    xp = x + (w - pw) // 2                          # centraliza o painel na área livre
    slot = (pw - 4) // 3                            # cada coluna ganha um "slot"; a caixa fica no meio dele
    cw = max(MIN_CARTA, min(int(slot * ESCALA_CARTA), slot - MIN_FOLGA))   # largura das cartas
    bw = slot - MIN_FOLGA                           # largura dos botões (mais largos que as cartas)

    moldura(xp, y_painel, pw, ph)

    larguras = [cw, cw, cw]
    xs = [xp + 2 + i * slot + (slot - cw) // 2 for i in range(3)]
    xb = xp + 2 + (slot - bw) // 2                  # x dos botões (primeira coluna)
    y1 = y_painel + 2
    y2 = y1 + h1 + gap_v

    def cor_de(preco, cor):         # sem dinheiro suficiente = caixa cinza
        return cor if estado.dinheiro >= preco else W.DARKGRAY

    # fileira 1: botões (empilhados) + 2 itens
    hb1 = (h1 - ESPACO) // 2
    hb2 = h1 - ESPACO - hb1
    caixa(xb, y1, bw, hb1, ["Próxima", "Rodada"],
          cor=W.LIGHTRED, selecionado=(selecionado == 0))
    caixa(xb, y1 + hb1 + ESPACO, bw, hb2, ["Reroll", f"${loja['reroll']}"],
          cor=cor_de(loja["reroll"], W.LIGHTGREEN), selecionado=(selecionado == 1))
    for i, item in enumerate(loja["itens"]):
        caixa(xs[1 + i], y1, larguras[1 + i], h1, [item["nome"], item["tipo"]],
              cor=cor_de(item["preco"], W.WHITE), preco=item["preco"],
              tecla=TECLAS_COMPRA["item"][i].upper())

    # fileira 2: voucher + 2 pacotes
    v = loja["voucher"]
    caixa(xs[0], y2, larguras[0], h2, [v["nome"], v["tipo"]],
          cor=cor_de(v["preco"], W.LIGHTCYAN), preco=v["preco"],
          tecla=TECLAS_COMPRA["voucher"][0].upper())
    for i, p in enumerate(loja["pacotes"]):
        caixa(xs[1 + i], y2, larguras[1 + i], h2, [p["nome"], p["tipo"]],
              cor=cor_de(p["preco"], W.LIGHTMAGENTA), preco=p["preco"],
              tecla=TECLAS_COMPRA["pacote"][i].upper())
    return True


def preco_da_acao(loja, acao, indice):
    """Quanto custa a ação escolhida (0 para Próxima Rodada)."""
    if acao == "proxima":
        return 0
    if acao == "reroll":
        return loja["reroll"]
    if acao == "item":
        return loja["itens"][indice]["preco"]
    if acao == "voucher":
        return loja["voucher"]["preco"]
    return loja["pacotes"][indice]["preco"]


def rodar_loja(estado, x, y=2, loja=LOJA_EXEMPLO):
    """Loop da loja: espera tecla, atualiza e redesenha.
    - W ou seta para cima = Próxima Rodada; S ou seta para baixo = Reroll; Enter confirma.
    - As letras de TECLAS_COMPRA escolhem item, voucher e pacotes direto.
    Devolve (acao, indice): ("proxima", 0), ("reroll", 0), ("item", 0 ou 1), ("voucher", 0), ("pacote", 0 ou 1).
    Quem chama aplica o efeito (tirar dinheiro, sortear de novo...). Ações que o jogador não pode pagar são ignoradas."""
    W.setcursortype(W._NOCURSOR)
    selecionado = 0
    while True:
        desenhou = desenhar_loja(estado, x, y, loja, selecionado)
        codigo, letra = W.getch()
        letra = letra.lower() if letra else ""
        if not desenhou:                    # terminal pequeno: espera o jogador aumentar a janela
            continue

        acao = None
        if codigo == SETA_CIMA or letra == "w":
            selecionado = 0
        elif codigo == SETA_BAIXO or letra == "s":
            selecionado = 1
        elif codigo == ENTER:
            acao = ("proxima", 0) if selecionado == 0 else ("reroll", 0)
        elif letra in LETRA_PARA_ACAO:
            acao = LETRA_PARA_ACAO[letra]

        if acao and estado.dinheiro >= preco_da_acao(loja, *acao):
            return acao