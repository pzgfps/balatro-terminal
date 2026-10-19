import random
import WConio2 as W
from WConio2 import *

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

OPCOES_MENU = ["Continuar", "Novo Jogo", "Configurações"]   # lista constante para mostrar as opções da aba menu
OPCOES_CONFIG = ["Voltar", "Sair"]                          # lista constante para mostrar as opções da aba de configurações

ALTURA, LARGURA = 48, 208           # a altura máxima é 30 e a largura é 145 (aparentemente)

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] # uma lista pra criar o poder de rank das cartas 
                                                                           # quanto maior o indice, maior o poder

NAIPES = {                  # isso aqui é um dicionario, não uma lista, onde ela diz o naipe e a cor das cartas
    "copas"  : ("♥", W.RED),     # o RED e o BLACK são da biblioteca WConio2
    "ouros"  : ("♦", W.RED),
    "paus"   : ("♣", W.BLACK),
    "espadas": ("♠", W.BLACK)
}

def escrever(texto):                            # é necessário criar uma função de "escrever" pois o cputs não suporte imagens de 3 bytes
    print(texto, end="", flush=True)            # e é um saco ter que colocar esse end="", flush=True toda vez

def criar_baralho():    # função para criar um baralho embaralhado
    baralho = [(rank, naipe) for naipe in NAIPES for rank in RANKS] # o rank e o naipe são constantes (o define em C quase)
    random.shuffle(baralho)
    return baralho

def desenhar_logo():        # função pra desenhar a logo na tela 
    x, y = 76, 4
    for i, texto in enumerate(LOGO_BALATRO):
        W.gotoxy(x, y + i)
        escrever(texto)

def borda():           # essa função serve pra criar as bordas do menu (as linhas horizontas e verticais "delimitantes")
    W.gotoxy(1,1)
    escrever(LARGURA * "-")
    for linha in range(ALTURA):
        W.gotoxy(1, 2 + linha)
        escrever("|" + (LARGURA - 2) * " " + "|")
    W.gotoxy(1, 2 + ALTURA)
    escrever(LARGURA * "-")

def menu_opcoes(selecionada):          # função que serve para mostrar as opções do menu (Continuar jogo, Novo Jogo e Configurações)
    for i, texto in enumerate(OPCOES_MENU):
        W.gotoxy(94, 25 + i * 1)
        if i == selecionada:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(22))
        W.textbackground(W.BLACK)
        W.textcolor(W.LIGHTGRAY)

def config_opcoes(selecionada):                 # é necessário criar uma função pra mostrar as opções do menu e a animação de escolha
    for i, texto in enumerate(OPCOES_CONFIG):
        W.gotoxy(94, 25 + i * 1)
        if i == selecionada:
            W.textbackground(W.LIGHTGRAY)
            W.textcolor(W.BLACK)
        escrever(texto.center(22))
        W.textbackground(W.BLACK)
        W.textcolor(W.LIGHTGRAY)
        
def menu():             # essa função serve para chamar as funções de borda_menu e opcoes_menu (ela cria o menu de uma vez)
    W.clrscr()          # limpa a tela
    W.setcursortype(W._NOCURSOR)        # tira o cursor
    borda()                             # desenha a borda
    desenhar_logo()                     # desenha a logo
    selecionada = 0                     # cria a variável selecionada que é usada na funcao menu_opcoes
    while (True):
        menu_opcoes(selecionada)        
        codigo, letra = W.getch()                 # pega o valor da tecla
        if codigo == 72 or letra == "w":          # se a tecla for o w
            selecionada = (selecionada - 1) % len(OPCOES_MENU)      
        elif codigo == 80 or letra == "s":        # se a tecla for s
            selecionada = (selecionada + 1) % len(OPCOES_MENU)
        elif codigo == 13:                        # se a tecla for enter
            return selecionada

def config():
    W.clrscr()
    W.setcursortype(W._NOCURSOR)
    borda()
    selecionada = 0
    while(True): 
        config_opcoes(selecionada)
        codigo, letra = W.getch()
        if codigo == 72 or letra == "w":
            selecionada = (selecionada - 1) % len(OPCOES_CONFIG)
        elif codigo == 80 or letra == "s":
            selecionada = (selecionada + 1) % len(OPCOES_CONFIG)
        elif codigo == 13:
            return selecionada
    

opcao = menu()
if opcao == 0:
    print("Você escolheu continuar o jogo") # testar se a opção esta indo certa
    pass   # continuar jogo
elif opcao == 1:
    print("Você escolheu iniciar um novo jogo") # testar se a opção esta indo certa
    pass   # novo jogo
elif opcao == 2:
    if config() == 1: 
        pass
