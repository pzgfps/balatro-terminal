from configs.rules.baralho import criar_baralho
from configs.rules.carta import desenhar_mao
from configs.rules.tipo_de_mao import is_flush
from configs.rules.tipo_de_mao import is_sequencia
from configs.rules.carta import Carta

maoJogador = [Carta("A", "espadas"), Carta("2", "espadas"), Carta("3", "espadas"), Carta("4", "espadas"),
              Carta("5", "espadas")]    # as 8 primeiras cartas

desenhar_mao(maoJogador)
if is_flush(maoJogador) == True:
  print("A mao é um flush!")
else:
  print("A mao não é um flush!")

if is_sequencia(maoJogador) == True:
  print("A mao é uma sequencia!")