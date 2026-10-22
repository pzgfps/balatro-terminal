import WConio2 as W
from configs.config import LARGURA_BORDA, OPCOES_CONFIG, OPCOES_MENU, LARGURA_BOTAO, ESPACO_BOTOES_MENU
from assets.art.art import LOGO_BALATRO, desenhar_logo, borda, escrever

def desenhar_opcoes(OPCOES, selecionada):       # funcao para desenhar as opcoes (para alterar as opcoes basta alterar o parametro OPCOES)
    total = len(OPCOES) * LARGURA_BOTAO + (len(OPCOES) - 1) * ESPACO_BOTOES_MENU    # serve para descobrir a largura do espaço necessário pros botões e o espaço entre eles
    x = (LARGURA_BORDA - total) // 2 + 1              # largura_borda pega o valor maximo da largura do cmd e subtrai da quantidade do espaço dos botoes
    y = 3 + len(LOGO_BALATRO) + 2               # o +3 serve para aumentar o valor de y (linha aonde as opcoes vao aparecer) já que a logo começa na posição 3
                                                # o len(LOGO_BALATRO) serve para para calcular quantas linhas a logo ocupa e o +2 para adicionar mais linhas entre
    for i, texto in enumerate(OPCOES):
        W.gotoxy(x + i * (LARGURA_BOTAO + ESPACO_BOTOES_MENU), y)     # serve para descobrir aonde em x, y vai inserir as opcoes (iniciar, novo jogo, config)
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
    W.clrscr()                       # limpa a tela
    W.setcursortype(W._NOCURSOR)     # tira o cursor do cmd
    borda()                          # desenha a borda do jogo
    desenhar_logo()                  # desenha a logo
    selecionada = 0                  # criacao da variavel selecionada que vai ser utilizada abaixo
    while(True):                     # ela vai ficar aparecendo/rodando até que uma opcao seja selecionada
        desenhar_opcoes(OPCOES_CONFIG, selecionada) # ele chama a funcao desenhar_opcoes pra completar a exibição do menu de configurações
        codigo, letra = W.getch()                   # vai pegar a tecla que o usuario digitou (vai pegar o codigo ASCII e a letra em char )
        if codigo == 75 or letra == 'a':
            selecionada = (selecionada - 1) % len(OPCOES_CONFIG)
        elif codigo == 77 or letra == 'd':
            selecionada = (selecionada + 1) % len(OPCOES_CONFIG)
        elif codigo == 13:
            return selecionada