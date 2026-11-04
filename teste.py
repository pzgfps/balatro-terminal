from configs.rules.carta import Carta
from configs.rules.carta import desenhar_mao
from configs.rules.tipo_de_mao import identificar_mao, MAOS
from configs.rules.baralho import criar_baralho, comprar_cartas
from configs.rules.coringa import CoringaJoker, CoringaMisprint, CoringaCavendish, CoringaMysticSummit

# 1. Par (K, K) -> is_par = True
##maoJogador = [Carta("K", "copas"), Carta("K", "espadas"), Carta("3", "ouros"), Carta("7", "paus"), Carta("9", "copas")]

# 2. Dois pares (4, 4 e J, J) -> is_dois_pares = True
##maoJogador = [Carta("4", "copas"), Carta("4", "paus"), Carta("J", "ouros"), Carta("J", "espadas"), Carta("2", "copas")]

# 3. Trinca (8, 8, 8) -> is_trinca = True
##maoJogador = [Carta("8", "copas"), Carta("8", "paus"), Carta("8", "ouros"), Carta("5", "espadas"), Carta("Q", "copas")]

# 4. Full House (K, K, K e 6, 6) -> is_full_house = True
##maoJogador = [Carta("K", "copas"), Carta("K", "paus"), Carta("K", "ouros"), Carta("6", "espadas"), Carta("6", "copas")]

# 5. Quadra (9, 9, 9, 9) -> is_quadra = True
##maoJogador = [Carta("9", "copas"), Carta("9", "paus"), Carta("9", "ouros"), Carta("9", "espadas"), Carta("A", "copas")]

maoJogador = []

baralho = criar_baralho()

comprar_cartas(maoJogador, baralho, 8)





coringasJogador = [CoringaMysticSummit()]

desenhar_mao(maoJogador)

jogada = maoJogador

nomeJogada = identificar_mao(jogada)

print(nomeJogada)

fichas, mult = MAOS[identificar_mao(maoJogador)]

print(f"Fichas: {fichas} Mult: {mult}")
pontuacao = 0

print(f"Pontuacao: {pontuacao}")

descarte = 0
for coringa in coringasJogador:
    mult = coringa.efeito(pontuacao, mult, descarte)
    

print(f"Mult após o efeito dos Coringas: {mult}")
pontuacao = (fichas * mult)
print(f"Pontuacao Final: {pontuacao}")

