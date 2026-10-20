import WConio2 as W
from config import ALTURA, LARGURA
from interface.tela import escrever

def escrever(texto):                            # é necessário criar uma função de "escrever" pois o cputs não suporte imagens de 3 bytes
    print(texto, end="", flush=True)            # e é um saco ter que colocar esse end="", flush=True toda vez

def borda():           # essa função serve pra criar as bordas do menu (as linhas horizontas e verticais "delimitantes")
    W.gotoxy(1,1)
    escrever(LARGURA * "-")
    for linha in range(ALTURA):
        W.gotoxy(1, 2 + linha)
        escrever("|" + (LARGURA - 2) * " " + "|")
    W.gotoxy(1, 2 + ALTURA)
    escrever(LARGURA * "-")

LOGO_BALATRO = [
    "|--------------------------------------------------------|",
    "|                                                        |",
    "|    █████   ████  ██      ████  ██████ █████   ████     |",
    "|    ██  ██ ██  ██ ██     ██  ██   ██   ██  ██ ██  ██    |",
    "|    ██  ██ ██  ██ ██     ██  ██   ██   ██  ██ ██  ██    |",
    "|    █████  ██████ ██     ██████   ██   █████  ██  ██    |",
    "|    ██  ██ ██  ██ ██     ██  ██   ██   ██ ██  ██  ██    |",
    "|    ██  ██ ██  ██ ██     ██  ██   ██   ██  ██ ██  ██    |",
    "|    █████  ██  ██ ██████ ██  ██   ██   ██  ██  ████     |",
    "|                                                        |",
    "|--------------------------------------------------------|"
]

MENU_LATERAL = [
    "╔════════════════════════╗",
    "║      ESCOLHA SEU       ║",
    "║     PROXIMO BLIND      ║",
    "║                        ║",
    "║════════════════════════║",
    "║  Pontuação:            ║",
    "║    Fichas  x   Mult    ║",
    "║                        ║",
    "║════════════════════════║",
    "║   Maos:     Descart:   ║",
    "║                        ║",
    "║════════════════════════║",
    "║  Dinheiro: $           ║",
    "╚════════════════════════╝",
]

def desenhar_logo():            # funcao pra desenhar a logo
    largura_logo = len(LOGO_BALATRO[0]) # mede o tamanho da primeira linha da logo, pois
                                        # todas as linhas tem o mesmo tamanho
    x = (LARGURA - largura_logo) // 2 + 1
    y = 3
    for i, texto in enumerate(LOGO_BALATRO):
        W.gotoxy(x, y + i)
        escrever(texto)

def desenhar_menu_lateral():
    largura_menu_lateral = len(MENU_LATERAL[0])

    x = (LARGURA - largura_menu_lateral) // 2 + 1
    y = 3
    for i, texto in enumerate(MENU_LATERAL):
        W.gotoxy(x, y + i)
        escrever(texto)