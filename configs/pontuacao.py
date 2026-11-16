from configs.rules.tipo_de_mao import identificar_mao, identificar_valores, MAOS    # funcoes e tabela que ja existem

# este arquivo junta tudo que antes estava repetido em teste.py e teste_maos_coringas.py

# ----------------------------------------------------Calcular a pontuacao------------------------------------------------------#

def calcular_pontuacao(cartas_jogadas, coringas, descartes):    # so calcula e devolve (nao mexe em nada do jogo)
    nome = identificar_mao(cartas_jogadas)      # descobre qual e a mao (ex: "Par"); devolve None se nao tem cartas
    if nome is None:                            # sem cartas nao tem pontuacao
        return None, 0, 0, 0
    fichas, mult = MAOS[nome]                   # fichas e mult base dessa mao, vindos do dicionario MAOS
    fichas = identificar_valores(cartas_jogadas, fichas)    # soma o valor de TODAS as cartas jogadas nas fichas (J, Q, K e A valem 10)
    for coringa in coringas:                    # cada coringa mexe no mult, um depois do outro (a ordem da lista muda o resultado)
        mult = coringa.efeito(fichas, mult, descartes)
    pontos = fichas * mult                      # pontuacao final da jogada
    return nome, fichas, mult, pontos

def pontuar_jogada(estado, cartas_jogadas, coringas):       # calcula e ja atualiza o estado (o menu lateral le esses valores)
    nome, fichas, mult, pontos = calcular_pontuacao(cartas_jogadas, coringas, estado.descartes)
    estado.fichas = fichas                      # mostra as fichas dessa jogada no menu lateral
    estado.mult = mult                          # mostra o mult dessa jogada no menu lateral
    estado.pontos += pontos                     # SOMA na pontuacao da rodada (as jogadas se acumulam)
    return nome, pontos                         # devolve o nome da mao e os pontos ganhos, pra tela poder mostrar

# ------------------------------------------------------------------------------------------------------------------------------#
