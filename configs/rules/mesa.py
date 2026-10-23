import random   # biblioteca para a randomização de numeros e do baralho
from assets.art.carta import Carta, Naipe, Rank

def criar_baralho(): # funcao para criar a "mesa" com 52 cartas unicas e devolve embaralhadas

    baralho = [Carta(naipe, rank) for naipe in Naipe for rank in Rank]
    random.shuffle(baralho)
    return baralho