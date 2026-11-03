from collections import Counter

from configs.config import VALORES

MAOS = {
    "Carta Alta":     (5, 1),
    "Par":            (10, 2),
    "Dois Pares":     (20, 2),
    "Trinca":         (30, 3),
    "Sequência":      (30, 4),
    "Flush":          (35, 4),
    "Full House":     (40, 4),
    "Quadra":         (60, 7),
    "Straight Flush": (100, 8)
}

def is_par(cartas):
    contagem = {}

    


def is_flush(cartas):
    if len(cartas) != 5:      #um flush deve ter 5 cartas
      return False

    naipe = cartas[0].naipe
    for carta in cartas:
        if carta.naipe != naipe:
          return False
    return True 

def is_sequencia(cartas):
    if len(cartas) != 5:      #uma sequencia deve ter 5 cartas
      return False
    
    posicoes = []           #criando uma lista das cartas ordenadas
    for carta in cartas:
        posicoes.append(VALORES.index(carta.valor))   #retorna o indice da carta
    posicoes.sort() 

    if posicoes == [0, 1, 2, 3, 12]:
        return True

    for i in range(1, 5):
        if posicoes[i] != posicoes[i - 1] + 1:#se o numero anterior nao é igual ao numero referente - 1 ele retorna falso
            return False
    return True

def identificar_mao():

    sequencia = is_sequencia
    flush = is_flus

    if sequencia and flush:
      return "Straight Flush"
