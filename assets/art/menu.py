import WConio2 as W
from configs.config import LARGURA_BORDA, LARGURA_OPCAO, OPCOES_CONFIG, OPCOES_MENU, LARGURA_BOTAO, ESPACO
from assets.art.art import LOGO_BALATRO, desenhar_logo, borda, escrever

def desenhar_opcoes(OPCOES, selecionada):       # funcao para desenhar as opcoes (para alterar as opcoes basta alterar o parametro OPCOES)
    total = len(OPCOES) * LARGURA_BOTAO + (len(OPCOES) - 1) * ESPACO
    x = (LARGURA_BORDA - total) // 2 + 1              # centraliza o conjunto de botões
    y = 3 + len(LOGO_BALATRO) + 2               # linha das opções (fixa)
    
    for i, texto in enumerate(OPCOES):
        W.gotoxy(x + i * (LARGURA_BOTAO + ESPACO), y)     # y fixo, só o x muda
        if i == selecionada:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(LARGURA_BOTAO))
        W.textbackground(W.BLACK)
        W.textcolor(W.LIGHTGRAY)

def menu_inicial():             # essa função serve para chamar as funções de borda() e desenhar_opcoes() (ela cria o menu de uma vez)
    W.clrscr()                  # limpa a tela
    W.setcursortype(W._NOCURSOR)        # tira o cursor
    borda()                             # desenha a borda
    desenhar_logo()                     # desenha a logo
    selecionada = 0                     # cria a variável selecionada que é usada na funcao desenhar_opcoes
    while (True):
        desenhar_opcoes(OPCOES_MENU, selecionada)        
        codigo, letra = W.getch()                 # pega o valor da tecla
        if codigo == 75 or letra == "a":          # se a tecla for o w
            selecionada = (selecionada - 1) % len(OPCOES_MENU)      
        elif codigo == 77 or letra == "d":        # se a tecla for s
            selecionada = (selecionada + 1) % len(OPCOES_MENU)
        elif codigo == 13:                        # se a tecla for enter
            return selecionada

def menu_configuracoes():            # funcao para criar o menu de configuracoes
    W.clrscr()
    W.setcursortype(W._NOCURSOR)
    borda()
    desenhar_logo()  
    selecionada = 0
    while(True): 
        desenhar_opcoes(OPCOES_CONFIG, selecionada)
        codigo, letra = W.getch()
        if codigo == 75 or letra == "a":
            selecionada = (selecionada - 1) % len(OPCOES_CONFIG)
        elif codigo == 77 or letra == "d":
            selecionada = (selecionada + 1) % len(OPCOES_CONFIG)
        elif codigo == 13:
            return selecionada