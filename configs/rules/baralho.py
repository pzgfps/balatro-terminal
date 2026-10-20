import random   # biblioteca para a randomização de numeros e do baralho

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] # uma lista pra criar o poder de rank das cartas 
                                                                           # quanto maior o indice, maior o poder

NAIPES = {
    "copas": "♥",
    "ouros": "♦",
    "paus": "♣",
    "espadas": "♠"
}

def criar_baralho():    # função para criar um baralho embaralhado
    baralho = [(rank, naipe) for naipe in NAIPES for rank in RANKS] # o rank e o naipe são constantes (o define em C quase)
    random.shuffle(baralho)
    return baralho