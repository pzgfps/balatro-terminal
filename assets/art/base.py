import WConio2 as W
from configs.config import LARGURA_BORDA, ALTURA_BORDA

# --------------------------------------------------Funções principais---------------------------------------------------------#

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

# -----------------------------------------------------------------------------------------------------------------------------#


# Vale a pena verificar se o nome base é bom ou não