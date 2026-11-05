from collections import Counter

from configs.config import VALORES

MAOS = {                                   #um dicionario que é acessado pelo nome da jogada e devolve o número de fichas e o mult que ela pontua
    "Carta Alta":     (5, 1),
    "Par":            (10, 2),
    "Dois Pares":     (20, 2),
    "Trinca":         (30, 3),
    "Sequência":      (30, 4),
    "Flush":          (35, 4),
    "Full House":     (40, 4),
    "Quadra":         (60, 7),
    "Straight Flush": (100, 8),
    "Royal Flush":    (100, 8)
}

def identificar_valores(cartas, fichas):
    for carta in cartas: 
        if carta.valor == "J" or carta.valor == "Q" or carta.valor == "K" or carta.valor == "A":
            fichas += 10
        else:
            fichas += int(carta.valor)
    return fichas

# cada funcao is_ confere se as cartas formam EXATAMENTE aquela mao (ex: um Full House nao conta como Par nem como Trinca)

def contar_repeticoes(cartas):      # conta quantas vezes cada valor aparece nas cartas e devolve so as quantidades
    contagem = Counter(carta.valor for carta in cartas)     # o Counter cria um dicionario, ex: tres Reis e dois 6 -> {"K": 3, "6": 2}
    return list(contagem.values())                          # pega so as quantidades, ex: [3, 2] (o valor da carta nao importa, so quantas vezes repete)

def is_par(cartas):
    repeticoes = contar_repeticoes(cartas)
    return repeticoes.count(2) == 1 and 3 not in repeticoes     # tem um (e so um) valor repetido 2 vezes, e nao é Full House (que tem um 3)

def is_dois_pares(cartas):
    repeticoes = contar_repeticoes(cartas)
    return repeticoes.count(2) == 2                             # dois valores diferentes repetidos 2 vezes cada

def is_trinca(cartas):
    repeticoes = contar_repeticoes(cartas)
    return 3 in repeticoes and 2 not in repeticoes              # tem um valor repetido 3 vezes e nao tem par junto (se tivesse seria Full House)

def is_full_house(cartas):
    repeticoes = contar_repeticoes(cartas)
    return 3 in repeticoes and 2 in repeticoes                  # uma trinca e um par juntos

def is_quadra(cartas):
    repeticoes = contar_repeticoes(cartas)
    return 4 in repeticoes                                      # um valor repetido 4 vezes (a quinta carta, se tiver, nao importa)

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

def is_straight_flush(cartas):
    return is_flush(cartas) and is_sequencia(cartas)            # as duas coisas ao mesmo tempo: mesmo naipe e em sequencia

def is_royal_flush(cartas):
    if not is_straight_flush(cartas):                           # primeiro tem que ser um Straight Flush
        return False
    valores = {carta.valor for carta in cartas}                 # as {} criam um conjunto com os valores das cartas (sem ordem)
    return valores == {"10", "J", "Q", "K", "A"}                # e os valores tem que ser exatamente esses (a sequencia mais alta)

def identificar_mao(cartas):    # recebe as cartas jogadas e devolve o NOME da mao (o mesmo nome que esta no dicionario MAOS)
    if len(cartas) == 0:        # sem cartas nao tem mao
        return None

    # a ordem importa: vai da mao mais forte pra mais fraca. Assim um Straight Flush nao é confundido com um Flush ou com uma Sequência
    if is_royal_flush(cartas):
        return "Royal Flush"
    if is_straight_flush(cartas):
        return "Straight Flush"
    if is_quadra(cartas):
        return "Quadra"
    if is_full_house(cartas):
        return "Full House"
    if is_flush(cartas):
        return "Flush"
    if is_sequencia(cartas):
        return "Sequência"
    if is_trinca(cartas):
        return "Trinca"
    if is_dois_pares(cartas):
        return "Dois Pares"
    if is_par(cartas):
        return "Par"
    return "Carta Alta"         # se nenhuma das de cima deu certo, sobrou a Carta Alta (por isso ela nao precisa de uma funcao is_)
