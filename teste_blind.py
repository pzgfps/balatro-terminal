from configs.estado import Estado
from configs.rules.carta import Carta
from configs.rules.blind import criar_blinds, total_de_rodadas, iniciar_blind, checar_rodada, finalizar_blind
from configs.pontuacao import pontuar_jogada

# ===== CRIAR AS BLINDS =====
for rodada in range(1, total_de_rodadas() + 1):
    blinds = criar_blinds(rodada)
    print("rodada", rodada, ":", [(b.nome, b.meta, b.recompensa) for b in blinds])
    assert [b.nome for b in blinds] == ["Small", "Big", "Boss"]
assert [b.meta for b in criar_blinds(1)] == [300, 450, 600]
assert [b.meta for b in criar_blinds(2)] == [800, 1200, 1600]
assert [b.meta for b in criar_blinds(3)] == [2000, 3000, 4000]
print("criar blinds ok")

# ===== INICIAR =====
estado = Estado()
estado.pontos = 999
estado.maos = 1
estado.descartes = 0
iniciar_blind(estado)
assert estado.pontos == 0 and estado.maos == 4 and estado.descartes == 3
print("iniciar ok")

# ===== VITORIA, DERROTA E RECOMPENSA =====
par = [Carta("K", "copas"), Carta("K", "paus"), Carta("3", "ouros"), Carta("7", "paus"), Carta("9", "copas")]     # Par que vale 98 pontos
estado = Estado()
small = criar_blinds(1)[0]                          # meta 300
iniciar_blind(estado)
assert checar_rodada(estado, small) == "continua"
pontuar_jogada(estado, par, [])                     # 98 pontos
pontuar_jogada(estado, par, [])                     # 196
estado.maos = 2
assert checar_rodada(estado, small) == "continua"
pontuar_jogada(estado, par, [])                     # 294
pontuar_jogada(estado, par, [])                     # 392
assert checar_rodada(estado, small) == "vitoria"
dinheiro_antes = estado.dinheiro
ganho = finalizar_blind(estado, small)
assert ganho == 3 + estado.maos and estado.dinheiro == dinheiro_antes + ganho
print("vitoria ok: ganhou $", ganho, "| dinheiro:", estado.dinheiro)

estado = Estado()
iniciar_blind(estado)
estado.maos = 0
assert checar_rodada(estado, small) == "derrota"
print("derrota ok")
print("\nTUDO OK")
