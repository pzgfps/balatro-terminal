import WConio2 as W
from config import LARGURA, LARGURA_OPCAO, OPCOES_CONFIG, OPCOES_MENU
from interface.art import LOGO_BALATRO, desenhar_logo
from interface.tela import borda, escrever

''' def menu_opcoes(selecionada):          # função que serve para mostrar as opções do menu (Continuar jogo, Novo Jogo e Configurações)    
    x = (LARGURA - LARGURA_OPCAO) // 2 + 1
    y = 3 + len(LOGO_BALATRO) + 2
    for i, texto in enumerate(OPCOES_MENU):
        W.gotoxy(x, y + i)
        if i == selecionada:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(30))
        W.textbackground(W.BLACK)
        W.textcolor(W.LIGHTGRAY)

def config_opcoes(selecionada):                 # é necessário criar uma função pra mostrar as opções do menu e a animação de escolha
    x = (LARGURA - LARGURA_OPCAO) // 2 + 1

    y = 3 + len(LOGO_BALATRO) + 2
    for i, texto in enumerate(OPCOES_CONFIG):
        W.gotoxy(x, y + i)
        if i == selecionada:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(30))
        W.textbackground(W.BLACK)
        W.textcolor(W.LIGHTGRAY) '''

# as duas funcoes acima foram unificadas em desenhar_opcoes, porque elas faziam a mesma coisa,
# e só mostravam listas diferentes (OPCOES_MENU, OPCOES_CONFIG), ai as listas viram parametro

def desenhar_opcoes(OPCOES, selecionada):
    x = (LARGURA - LARGURA_OPCAO) // 2 + 1
    y = 3 + len(LOGO_BALATRO) + 2

    for i, texto in enumerate(OPCOES):
        W.gotoxy(x, y + i)
        if i == selecionada:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(LARGURA_OPCAO))
        W.textbackground(W.BLACK)
        W.textcolor(W.LIGHTGRAY)

def menu():             # essa função serve para chamar as funções de borda_menu e opcoes_menu (ela cria o menu de uma vez)
    W.clrscr()          # limpa a tela
    W.setcursortype(W._NOCURSOR)        # tira o cursor
    borda()                             # desenha a borda
    desenhar_logo()                     # desenha a logo
    selecionada = 0                     # cria a variável selecionada que é usada na funcao menu_opcoes
    while (True):
        desenhar_opcoes(OPCOES_MENU, selecionada)        
        codigo, letra = W.getch()                 # pega o valor da tecla
        if codigo == 72 or letra == "w":          # se a tecla for o w
            selecionada = (selecionada - 1) % len(OPCOES_MENU)      
        elif codigo == 80 or letra == "s":        # se a tecla for s
            selecionada = (selecionada + 1) % len(OPCOES_MENU)
        elif codigo == 13:                        # se a tecla for enter
            return selecionada

def configuracoes():
    W.clrscr()
    W.setcursortype(W._NOCURSOR)
    borda()
    desenhar_logo()  
    selecionada = 0
    while(True): 
        desenhar_opcoes(OPCOES_CONFIG, selecionada)
        codigo, letra = W.getch()
        if codigo == 72 or letra == "w":
            selecionada = (selecionada - 1) % len(OPCOES_CONFIG)
        elif codigo == 80 or letra == "s":
            selecionada = (selecionada + 1) % len(OPCOES_CONFIG)
        elif codigo == 13:
            return selecionada