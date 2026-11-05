import WConio2 as W
import shutil # pega o tamanho do terminal (mesma biblioteca usada no config.py)

from configs.config import LARGURA_MENU_LATERAL
from assets.art.base import escrever

# ----------------------------------------------Função desenhar menu lateral---------------------------------------------------#

# pedaços fixos do menu lateral (o tamanho vem do config.py)
BORDA_SUPERIOR_MENU = "╔" + "═" * (LARGURA_MENU_LATERAL - 2) + "╗"   # - 2 porque os cantos já ocupam 2 espaços
BORDA_INFERIOR_MENU = "╚" + "═" * (LARGURA_MENU_LATERAL - 2) + "╝"
SEPARADOR_MENU = "╠" + "═" * (LARGURA_MENU_LATERAL - 2) + "╣"        # linha que divide uma seção da outra

def linha_menu(texto=""):       # monta UMA linha do menu: "║" + texto centralizado + "║" (sem texto = linha vazia)
    return "║" + texto.center(LARGURA_MENU_LATERAL - 2) + "║"

def desenhar_menu_lateral(x, y, e):     # os parametros sao: posicao x, posicao y e estado (objeto do estado.py com
                                        # pontos, fichas, mult, maos, descartes e dinheiro)
    altura = shutil.get_terminal_size().lines - y - 1   # linhas livres do y até o fim do terminal (-1 pra nao encostar no fim)

    # cada seção é uma lista de linhas de texto (o "" cria uma linha vazia)
    secoes = [
        ["", "Escolha seu", "próximo Blind", ""],
        ["", "Pontuação da Rodada", str(e.pontos), ""],   # str() pra transformar o número em texto
        ["", "Fichas   x   Mult", f"{e.fichas}   x   {e.mult}", ""],   # o f"" já junta os valores no texto
        ["", "Mãos     Descartes", f"{e.maos}           {e.descartes}", ""],
        ["", "", f"Dinheiro: ${e.dinheiro}", ""],
    ]

    # passo 1: contar o mínimo de linhas que o menu precisa (sem nenhum espaço extra)
    linhas_de_texto = sum(len(secao) for secao in secoes)   # soma o tamanho de todas as seções
    separadores = len(secoes) - 1                           # tem um separador entre cada seção (então 1 a menos que as seções)
    bordas = 2                                              # a de cima e a de baixo
    minimo = linhas_de_texto + separadores + bordas

    # passo 2: ver quantas linhas sobram no terminal e dividir entre as seções (o menu estica conforme o terminal)
    sobra = max(0, altura - minimo)     # max() pra nao ficar negativo se o terminal for pequeno
    por_secao, resto = divmod(sobra, len(secoes))   # exemplo: sobra 12 e 5 seções -> 2 pra cada seção e 2 que sobram
                                                    # (essas 2 viram 1 linha extra para as 2 primeiras seções)

    # passo 3: montar o menu de cima pra baixo numa lista de linhas
    linhas = [BORDA_SUPERIOR_MENU]
    for i, secao in enumerate(secoes):
        vazias = por_secao + (1 if i < resto else 0)    # linhas vazias dessa seção (+1 se ela está entre as primeiras que pegam o resto)
        acima = vazias // 2                             # metade fica em cima do texto e a outra metade embaixo,
        abaixo = vazias - acima                         # assim o texto fica centralizado na seção
        linhas += [linha_menu()] * acima
        linhas += [linha_menu(texto) for texto in secao]
        linhas += [linha_menu()] * abaixo
        if i < len(secoes) - 1:                         # o separador só vai entre seções (nao depois da última)
            linhas.append(SEPARADOR_MENU)
    linhas.append(BORDA_INFERIOR_MENU)

    # passo 4: desenhar de fato, cada linha uma posição abaixo da anterior
    for i, linha in enumerate(linhas):
        W.gotoxy(x, y + i)
        escrever(linha)

# -----------------------------------------------------------------------------------------------------------------------------#