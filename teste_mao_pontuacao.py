from configs.estado import Estado
from configs.config import TAMANHO_MAO
from configs.rules.carta import Carta
from configs.rules.baralho import criar_baralho, comprar_cartas
from configs.rules.coringa import CoringaJoker, CoringaCavendish
from configs.mao import alternar_selecao, descartar_cartas, jogar_cartas, ordenar_por_valor, ordenar_por_naipe
from configs.pontuacao import calcular_pontuacao, pontuar_jogada

# ===== SELECAO =====
selecionadas = []
alternar_selecao(selecionadas, 2)       # marca a 2
alternar_selecao(selecionadas, 5)       # marca a 5
alternar_selecao(selecionadas, 2)       # desmarca a 2
assert selecionadas == [5]
for i in range(8):                      # tenta marcar as 8 posicoes
    alternar_selecao(selecionadas, i)
assert len(selecionadas) == 5           # nao passa de 5
print("selecao ok:", selecionadas)

# ===== DESCARTAR E JOGAR =====
estado = Estado()
baralho = criar_baralho()
mao = []
comprar_cartas(mao, baralho, TAMANHO_MAO)
selecionadas = [0, 3]
descartadas = descartar_cartas(mao, selecionadas, baralho, estado)
assert len(descartadas) == 2 and len(mao) == TAMANHO_MAO and estado.descartes == 2 and selecionadas == []
print("descartar ok: descartes restantes =", estado.descartes)

selecionadas = [1, 2, 4]
jogadas = jogar_cartas(mao, selecionadas, baralho, estado)
assert len(jogadas) == 3 and len(mao) == TAMANHO_MAO and estado.maos == 3
print("jogar ok: maos restantes =", estado.maos, "| baralho:", len(baralho), "cartas")

estado.descartes = 0                    # sem descartes nao pode descartar
assert descartar_cartas(mao, [0], baralho, estado) == [] and len(mao) == TAMANHO_MAO
print("sem descartes ok")

# ===== ORDENAR =====
ordenar_por_valor(mao, [])
print("por valor: ", [c.descricao() for c in mao])
ordenar_por_naipe(mao, [])
print("por naipe: ", [c.descricao() for c in mao])

# ===== PONTUACAO (mesmos numeros do teste_maos_coringas.py) =====
par = [Carta("K", "copas"), Carta("K", "espadas"), Carta("3", "ouros"), Carta("7", "paus"), Carta("9", "copas")]
nome, fichas, mult, pontos = calcular_pontuacao(par, [], 3)
assert (nome, fichas, mult, pontos) == ("Par", 49, 2, 98)           # 10 + 10 + 10 + 3 + 7 + 9 = 49 fichas, 49 x 2 = 98
nome, fichas, mult, pontos = calcular_pontuacao(par, [CoringaJoker(), CoringaCavendish()], 3)
assert (mult, pontos) == (18, 882)                                  # mult 2 +4 = 6, x3 = 18 / 49 x 18 = 882
assert calcular_pontuacao([], [], 3) == (None, 0, 0, 0)
print("pontuacao ok:", nome, fichas, "x", mult, "=", pontos)

estado = Estado()
pontuar_jogada(estado, par, [])
pontuar_jogada(estado, par, [])
assert estado.pontos == 196 and estado.fichas == 49 and estado.mult == 2
print("estado ok: pontos da rodada =", estado.pontos)
print("\nTUDO OK")
