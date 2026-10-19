import WConio2 as W
from config import ALTURA, LARGURA

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