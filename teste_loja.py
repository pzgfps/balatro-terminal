from configs.rodada import criar_partida, blind_atual, iniciar_blind_atual
from configs.rules.carta import Carta
from configs.rules.coringa import Coringa, CoringaJoker
from configs.loja import gerar_loja, comprar_item, rerrolar_loja, aplicar_acao, PRECO_REROLL, MAX_CORINGAS, PRECO_INDISPONIVEL
from configs.pontuacao import pontuar_jogada

def item_joker():                                   # item fixo, pra o teste nao depender de sorteio
    return {"nome": "Joker", "tipo": "Coringa", "preco": 4, "classe": CoringaJoker}

# ===== GERAR A LOJA =====
loja = gerar_loja()
assert loja["reroll"] == PRECO_REROLL and len(loja["itens"]) == 2 and len(loja["pacotes"]) == 2
assert all(i["tipo"] == "Coringa" and i["preco"] > 0 for i in loja["itens"])
assert loja["voucher"]["preco"] == PRECO_INDISPONIVEL and all(p["preco"] == PRECO_INDISPONIVEL for p in loja["pacotes"])
print("gerar loja ok:", [i["nome"] for i in loja["itens"]])

# ===== COMPRAR =====
partida = criar_partida()
partida.estado.dinheiro = 10
loja = gerar_loja()
loja["itens"][0] = item_joker()
assert comprar_item(partida, loja, 0) == "ok"
assert partida.estado.dinheiro == 6 and len(partida.coringas) == 1 and isinstance(partida.coringas[0], Coringa)
assert loja["itens"][0]["nome"] == "Vendido" and len(loja["itens"]) == 2
assert comprar_item(partida, loja, 0) == "indisponivel"         # nao compra o mesmo slot duas vezes
assert partida.estado.dinheiro == 6 and len(partida.coringas) == 1
print("comprar ok")

# ===== SEM DINHEIRO E SEM ESPACO =====
partida = criar_partida()
partida.estado.dinheiro = 3
loja = gerar_loja()
loja["itens"][1] = item_joker()
assert comprar_item(partida, loja, 1) == "sem_dinheiro"
assert partida.estado.dinheiro == 3 and len(partida.coringas) == 0 and loja["itens"][1]["nome"] == "Joker"
partida.estado.dinheiro = 50
partida.coringas = [CoringaJoker() for i in range(MAX_CORINGAS)]
assert comprar_item(partida, loja, 1) == "sem_espaco"
assert partida.estado.dinheiro == 50 and len(partida.coringas) == MAX_CORINGAS
print("sem dinheiro e sem espaco ok")

# ===== REROLL =====
partida = criar_partida()
partida.estado.dinheiro = 20
loja = gerar_loja()
loja["itens"][0] = item_joker()
comprar_item(partida, loja, 0)                                  # dinheiro 16, slot 0 "Vendido"
assert rerrolar_loja(partida, loja) == "ok"
assert partida.estado.dinheiro == 11 and loja["reroll"] == 6    # pagou $5, o proximo custa $6
assert loja["itens"][0]["tipo"] == "Coringa"                    # o slot vendido voltou a ter coringa
assert rerrolar_loja(partida, loja) == "ok"
assert partida.estado.dinheiro == 5 and loja["reroll"] == 7
assert rerrolar_loja(partida, loja) == "sem_dinheiro"           # $5 nao paga $7
assert partida.estado.dinheiro == 5 and loja["reroll"] == 7
assert len(partida.coringas) == 1                               # o coringa comprado continua com o jogador
print("reroll ok")

# ===== APLICAR ACAO (o que a tela devolve) =====
partida = criar_partida()
partida.estado.dinheiro = 10
loja = gerar_loja()
loja["itens"][1] = item_joker()
assert aplicar_acao(partida, loja, "item", 1) == "ok"
assert aplicar_acao(partida, loja, "reroll", 0) == "ok"
assert aplicar_acao(partida, loja, "voucher", 0) == "indisponivel"
assert aplicar_acao(partida, loja, "pacote", 1) == "indisponivel"
assert aplicar_acao(partida, loja, "proxima", 0) == "proxima"
print("aplicar acao ok")

# ===== O CORINGA COMPRADO ENTRA NA PONTUACAO =====
partida = criar_partida()
partida.estado.dinheiro = 10
loja = gerar_loja()
loja["itens"][0] = item_joker()
aplicar_acao(partida, loja, "item", 0)
iniciar_blind_atual(partida)
par = [Carta("K", "copas"), Carta("K", "paus"), Carta("3", "ouros"), Carta("7", "paus"), Carta("9", "copas")]
nome, pontos = pontuar_jogada(partida.estado, par, partida.coringas)
assert nome == "Par" and pontos == 49 * (2 + 4)                 # sem coringa seriam 98; com o Joker o mult vai de 2 pra 6
print("coringa comprado pontua ok:", pontos)
print("\nTUDO OK")
