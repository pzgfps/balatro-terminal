from configs.rules.carta import Carta
from configs.rules.tipo_de_mao import identificar_mao, MAOS
from configs.rules.coringa import CoringaJoker, CoringaCavendish, CoringaMysticSummit

# cada jogada é uma lista de cartas (o jogador pode jogar de 1 a 5)
jogadas = [
    [Carta("K", "copas"), Carta("7", "paus"), Carta("2", "ouros")],                                                   # carta alta
    [Carta("9", "copas"), Carta("9", "paus"), Carta("4", "ouros")],                                                   # par
    [Carta("5", "copas"), Carta("5", "paus"), Carta("J", "ouros"), Carta("J", "espadas")],                            # dois pares
    [Carta("Q", "copas"), Carta("Q", "paus"), Carta("Q", "ouros"), Carta("3", "espadas")],                            # trinca
    [Carta("A", "copas"), Carta("2", "paus"), Carta("3", "ouros"), Carta("4", "espadas"), Carta("5", "copas")],       # sequencia (o As vale 1 aqui)
    [Carta("2", "ouros"), Carta("6", "ouros"), Carta("9", "ouros"), Carta("J", "ouros"), Carta("K", "ouros")],        # flush
    [Carta("K", "copas"), Carta("K", "paus"), Carta("K", "ouros"), Carta("6", "espadas"), Carta("6", "copas")],       # full house
    [Carta("8", "copas"), Carta("8", "paus"), Carta("8", "ouros"), Carta("8", "espadas")],                            # quadra (so 4 cartas)
    [Carta("5", "paus"), Carta("6", "paus"), Carta("7", "paus"), Carta("8", "paus"), Carta("9", "paus")],             # straight flush
    [Carta("10", "espadas"), Carta("J", "espadas"), Carta("Q", "espadas"), Carta("K", "espadas"), Carta("A", "espadas")],   # royal flush
]

coringas = [CoringaJoker(), CoringaCavendish(), CoringaMysticSummit()]     # lista de coringas diferentes (polimorfismo: todos tem o efeito())
descartes = 0       # com 0 descartes o Cume Místico também ativa

for jogada in jogadas:
    nome = identificar_mao(jogada)      # descobre qual é a mao
    fichas, mult = MAOS[nome]           # pega as fichas e o mult dessa mao no dicionario
    pontos = fichas * mult              # pontuacao sem coringas

    for coringa in coringas:            # cada coringa mexe no mult, um depois do outro (a ordem muda o resultado!)
        mult = coringa.efeito(fichas, mult, descartes)
    pontos_com_coringas = fichas * mult

    print(f"{nome:15s} {fichas:>3} x {MAOS[nome][1]:<2} = {pontos:>4}   |   com coringas: {fichas:>3} x {mult:<3} = {pontos_com_coringas}")
