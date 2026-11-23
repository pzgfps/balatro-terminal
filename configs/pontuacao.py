from configs.config import TAMANHO_MAO
from configs.rules.baralho import comprar_cartas
from configs.rules.tipo_de_mao import MAOS, identificar_mao, identificar_valores


def calcular_jogada(jogada, coringas, descartes):       # so CALCULA: nao altera o estado do jogo (da pra usar como previa)
    nome = identificar_mao(jogada)                          # 1. que mao é?
    fichas, mult = MAOS[nome]                               # 2. valores base dessa mao
    fichas += identificar_valores(jogada, nome)             # 3. soma as cartas que contam

    for coringa in coringas:                                # 4. cada coringa mexe no mult, um depois do outro
        fichas = coringa.efeito_fichas(fichas, descartes)
        mult = coringa.efeito_mult(mult, descartes)

    return nome, fichas, mult, fichas * mult                # 5. devolve tudo pra tela poder mostrar


def jogar_mao(estado, mao_jogador, selecionadas, baralho, coringas):    # so MEXE no estado: pontos, jogadas e cartas da mao
    nome, fichas, mult, pontos = calcular_jogada(selecionadas, coringas, estado.descartes)

    estado.pontos += pontos
    estado.maos -= 1

    for carta in selecionadas:
        mao_jogador.remove(carta)                           # tira as cartas jogadas da mao
    comprar_cartas(mao_jogador, baralho, TAMANHO_MAO)       # repoe ate completar a mao

    return nome, fichas, mult, pontos