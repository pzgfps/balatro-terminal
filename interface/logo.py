import WConio2 as W
from config import LARGURA
from interface.tela import escrever


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

def desenhar_logo():            # funcao pra desenhar a logo
    largura_logo = len(LOGO_BALATRO[0]) # mede o tamanho da primeira linha da logo, pois
                                        # todas as linhas tem o mesmo tamanho
    x = (LARGURA - largura_logo) // 2 + 1
    y = 3
    for i, texto in enumerate(LOGO_BALATRO):
        W.gotoxy(x, y + i)
        escrever(texto)