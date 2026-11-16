from configs.config import MAX_JOGADAS, TAMANHO_MAO, VALORES, NAIPES      # constantes que ja existem no config.py
from configs.rules.baralho import comprar_cartas                          # funcao que repoe a mao com cartas do baralho

# este arquivo so tem logica (nada de print nem de tela): quem faz a tela so precisa chamar essas funcoes

# ----------------------------------------------------Selecionar cartas-------------------------------------------------------------#

def alternar_selecao(selecionadas, posicao):    # selecionadas: lista com as posicoes marcadas (ex: [0, 3]) / posicao: onde o cursor esta
    if posicao in selecionadas:                 # se a posicao ja esta marcada...
        selecionadas.remove(posicao)            # ...desmarca (tira da lista)
        return True                             # devolve True: a selecao mudou
    if len(selecionadas) >= MAX_JOGADAS:        # se nao estava marcada mas ja tem 5 marcadas...
        return False                            # ...nao deixa marcar mais e devolve False: nada mudou
    selecionadas.append(posicao)                # senao, marca (coloca no fim da lista)
    return True                                 # devolve True: a selecao mudou

# ------------------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------Tirar cartas da mao-------------------------------------------------------#

def retirar_cartas(mao, selecionadas):          # tira da mao as cartas marcadas e devolve elas (usada por descartar_cartas e jogar_cartas)
    posicoes = sorted(selecionadas)             # sorted() poe as posicoes em ordem crescente, ex: [5, 1] vira [1, 5]
    cartas_retiradas = []                       # lista que vai guardar as cartas tiradas
    for posicao in posicoes:                    # primeiro so COPIA as cartas, da esquerda pra direita
        cartas_retiradas.append(mao[posicao])
    for posicao in reversed(posicoes):          # depois apaga da mao de TRAS pra FRENTE, porque apagar a posicao 1 faria
        mao.pop(posicao)                        # a carta da posicao 5 virar posicao 4 e a gente apagaria a carta errada
    return cartas_retiradas

# ------------------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------Descartar e jogar---------------------------------------------------------#

def descartar_cartas(mao, selecionadas, baralho, estado):   # estado: objeto do estado.py (usa estado.descartes)
    if len(selecionadas) == 0 or estado.descartes <= 0:     # sem carta marcada ou sem descartes: nao faz nada
        return []                                           # devolve lista vazia: nada foi descartado
    cartas_descartadas = retirar_cartas(mao, selecionadas)  # tira as cartas marcadas da mao
    estado.descartes -= 1                                   # gasta 1 descarte (nao importa quantas cartas foram)
    comprar_cartas(mao, baralho, TAMANHO_MAO)               # repoe a mao ate ter 8 cartas de novo
    selecionadas.clear()                                    # limpa a selecao (as posicoes antigas nao valem mais)
    return cartas_descartadas

def jogar_cartas(mao, selecionadas, baralho, estado):       # estado: objeto do estado.py (usa estado.maos)
    if len(selecionadas) == 0 or estado.maos <= 0:          # sem carta marcada ou sem maos restantes: nao faz nada
        return []                                           # devolve lista vazia: nada foi jogado
    cartas_jogadas = retirar_cartas(mao, selecionadas)      # tira as cartas marcadas da mao
    estado.maos -= 1                                        # gasta 1 mao
    comprar_cartas(mao, baralho, TAMANHO_MAO)               # repoe a mao ate ter 8 cartas de novo
    selecionadas.clear()                                    # limpa a selecao
    return cartas_jogadas                                   # essas cartas vao pra pontuacao.py calcular os pontos

# ------------------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------Ordenar a mao-------------------------------------------------------------#

def chave_valor(carta):                         # a chave diz pro sort() COMO comparar duas cartas
    return VALORES.index(carta.valor)           # posicao do valor na lista VALORES (o "2" e 0 e o "A" e 12): quanto maior, mais forte

def chave_naipe(carta):                         # compara primeiro pelo naipe e, se forem iguais, pelo valor
    return (NAIPES.index(carta.naipe), VALORES.index(carta.valor))   # tupla: o Python compara o 1o item e so olha o 2o se empatar

def ordenar_por_valor(mao, selecionadas):       # do mais forte (A) pro mais fraco (2), como no Balatro
    mao.sort(key=chave_valor, reverse=True)     # sort() reorganiza a propria lista / reverse=True deixa do maior pro menor
    selecionadas.clear()                        # as cartas mudaram de posicao, entao a selecao antiga nao vale mais

def ordenar_por_naipe(mao, selecionadas):       # agrupa por naipe (na ordem da lista NAIPES) e dentro de cada naipe do menor pro maior
    mao.sort(key=chave_naipe)
    selecionadas.clear()

# ------------------------------------------------------------------------------------------------------------------------------#
