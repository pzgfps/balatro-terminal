import WConio2 as W
from configs.config import ALTURA_BORDA, LARGURA_BORDA
import os

def escrever(texto):                            # é necessário criar uma função de "escrever" pois o cputs não suporte imagens de 3 bytes
    print(texto, end="", flush=True)            # e é um saco ter que colocar esse end="", flush=True toda vez

def borda():           # essa função serve pra criar as bordas do menu (as linhas horizontas e verticais "delimitantes")
    W.gotoxy(1,1)
    escrever(LARGURA_BORDA * "-")     # pega a constante largura e multiplica "-" para a criação da borda superior
    for linha in range(ALTURA_BORDA): # pega a constante altura e usa-a em um for, porque a cada iteracao ela adiciona as bordas laterais
        W.gotoxy(1, 2 + linha)  # 1, a mais esquerda, 2 + linha (altura)
        escrever("|" + (LARGURA_BORDA - 2) * " " + "|") # escreve a borda esquerda, depois adiciona vários espaços vazios e depois a borda lateral direita
    W.gotoxy(1, 2 + ALTURA_BORDA)         
    escrever(LARGURA_BORDA * "-")     #  no final do for, ele escreve a borda inferior

LOGO_BALATRO = [ #possibilidade de logo 
    "                              ████                       ███             ███           ███████  ",
    " █████████           █████   ████       ███████████████████████████████████          ███████████",
    " ███████████       ████████ ████      ██████████████████████████████████████████    ██████ █████",
    " ████   ████      █████████████       ███████████████████    ████      ███████████  ████     ███",
    " ████   ███      ████  ████ ███       ████████████████████   ████      ███    █████ ████     ███",
    " ████ ████      █████  ████ ████      ████████████████████   ████      ███     ███  ████     ███",
    " ██████████     ████  █████ ████      █████████  █████████   ████      ███    ████  ████     ███",
    " ████████████   ███████████ ████      ███████       ██████   ████      ███   ████   ████     ███",
    " ██████  █████  ███████████ ████      ██████    ██   ██████  ████      ███ ██████   ████     ███",
    " █████     ████ ██████ ████ ███       █████████████████████  ████      ████████████ ████     ███",
    " █████      █████████  ████ ████      █████████████████████  ████      ██████ █████ ████     ███",
    " █████      ████████   ████ ████      █████████████████████  █████     ████     ████████     ███",
    " █████       ███████   ███  ███████████████████████████████  █████     ███      ████████   █████",
    " ███████████████████   ██   ████████████████████████████████ ████      ███      ███ ████████████",
    "████████████████████       ████      ██████████████          ███       ███      ██    ████████  ",
    "███████████     ███        ██        █                        █        ███      █               ",
    "                ██                                                     ██                       ",
]

MENU_LATERAL = [
    "╔══════════════════════════════════════╗",
    "║                                      ║",
    "║             ESCOLHA SEU              ║",
    "║            PROXIMO BLIND             ║",
    "║                                      ║",
    "╠══════════════════════════════════════╣",
    "║                                      ║",
    "║    Pontuação:                        ║",
    "║                                      ║",
    "║       Fichas    x    Mult            ║",
    "║                                      ║",
    "╠══════════════════════════════════════╣",
    "║                                      ║",
    "║       Maos:         Descartes:       ║",
    "║                                      ║",
    "╠══════════════════════════════════════╣",
    "║                                      ║",
    "║    Dinheiro: $                       ║",
    "║                                      ║",
    "╚══════════════════════════════════════╝",
]

def desenhar_logo():            # funcao pra desenhar a logo
    largura_logo = len(LOGO_BALATRO[0]) # mede o tamanho da primeira linha da logo, pois
                                        # todas as linhas tem o mesmo tamanho
    x = (LARGURA_BORDA - largura_logo) // 2 + 1       # ela pega a largura da borda
    y = 3
    for i, texto in enumerate(LOGO_BALATRO):
        W.gotoxy(x, y + i)
        escrever(texto)


L = 30  # largura do menu

def lin(t=""):      # 
    return "║" + t.center(L - 2) + "║"

SEP = "╠" + "═" * (L - 2) + "╣"     # ele desenha a borda lateral e a divisória (largura * "=")

def desenhar_menu_lateral(x, y, e):     # os parametros sao; posicao x, posicao y, e estado(objeto que tem os valores de:    
                                         # Pontuacao, fichas, mult, maos, descartes e dinheiro. Esta no arquivo estado.py)
    altura = os.get_terminal_size().lines - y - 1   # pega a altura do terminal e diminui pra nao ultrapssar a borda

    # seções: (linhas de conteúdo)
    secoes = [                      # listas dentro de uma lista, ("") serve para criar uma linha vazia
        ["", "Escolha seu", "próximo Blind", ""],       
        ["", "Pontuação da Rodada", str(e.pontos), ""], # transforma os pontos em string p imprimir
        ["", "Fichas   x   Mult", f"{e.fichas}   x   {e.mult}", ""], # f para formatar, ai nao precisa transformar em string
        ["", "Mãos     Descartes", f"{e.maos}           {e.descartes}", ""],
        ["", "", f"Dinheiro: ${e.dinheiro}", ""],
    ]

    total = 0   
    for s in secoes:    # for para descobrir quantas linhas e colunas deverao ser desenhadas
        total += len(s) # vai pegar o tamanho de cada lista
    usadas = total + (len(secoes) - 1) + 2  # ele pega quantas linhas ja estao "reservadas" para serem obrigatoriamente

    extra = max(0, altura - usadas)
    por_secao, resto = divmod(extra, len(secoes))

    linhas = ["╔" + "═" * (L - 2) + "╗"]
    for i, s in enumerate(secoes):
        vazias = por_secao + (1 if i < resto else 0)
        metade = vazias // 2
        linhas += [lin()] * metade
        linhas += [lin(t) for t in s]
        linhas += [lin()] * (vazias - metade)
        if i < len(secoes) - 1:
            linhas.append(SEP)
    linhas.append("╚" + "═" * (L - 2) + "╝")

    for i, linha in enumerate(linhas):
        W.gotoxy(x, y + i)
        escrever(linha)
