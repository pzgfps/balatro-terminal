from configs.rodada import criar_partida, blind_atual, iniciar_blind_atual, jogar_mao, descartar_mao, fechar_blind, jogo_acabou
from configs.mao import alternar_selecao
from configs.config import TAMANHO_MAO

# ===== PARTIDA NOVA =====
partida = criar_partida()
assert partida.rodada == 1 and partida.posicao_blind == 0 and partida.status == "loja"
assert blind_atual(partida).nome == "Small" and blind_atual(partida).meta == 300
print("criar partida ok")

# ===== INICIAR E DESCARTAR =====
iniciar_blind_atual(partida)
assert partida.status == "jogando" and len(partida.mao) == TAMANHO_MAO and partida.estado.maos == 4
assert jogar_mao(partida) is None                       # sem cartas marcadas nao joga
assert partida.estado.maos == 4
alternar_selecao(partida.selecionadas, 0)
alternar_selecao(partida.selecionadas, 1)
assert descartar_mao(partida) == 2 and partida.estado.descartes == 2 and len(partida.mao) == TAMANHO_MAO
print("iniciar e descartar ok")

# ===== DERROTA: acabam as maos sem bater a meta =====
blind_atual(partida).meta = 10 ** 9                     # meta impossivel
for i in range(4):
    assert partida.status == "jogando"
    alternar_selecao(partida.selecionadas, 0)
    resultado = jogar_mao(partida)
    assert resultado is not None
assert partida.estado.maos == 0 and partida.status == "derrota" and jogo_acabou(partida)
assert jogar_mao(partida) is None                       # depois da derrota nao joga mais
print("derrota ok")

# ===== VITORIA: jogo inteiro (3 rodadas x 3 blinds = 9 blinds) =====
partida = criar_partida()
dinheiro = partida.estado.dinheiro
for numero in range(9):
    assert partida.status == "loja"
    iniciar_blind_atual(partida)
    blind_atual(partida).meta = 1                       # meta facil, so pra testar o caminho do jogo
    alternar_selecao(partida.selecionadas, 0)
    jogar_mao(partida)
    assert partida.status == "vitoria_blind"
    ganho = fechar_blind(partida)
    assert ganho > 0
    dinheiro += ganho
    assert partida.estado.dinheiro == dinheiro
    assert fechar_blind(partida) == 0                   # fechar duas vezes nao paga duas vezes
assert partida.status == "fim_vitoria" and jogo_acabou(partida)
print("jogo completo ok: dinheiro final = $", partida.estado.dinheiro)

# ===== AS METAS SOBEM DE RODADA =====
partida = criar_partida()
metas = []
for numero in range(9):
    metas.append(blind_atual(partida).meta)
    iniciar_blind_atual(partida)
    blind_atual(partida).meta = 1
    alternar_selecao(partida.selecionadas, 0)
    jogar_mao(partida)
    fechar_blind(partida)
assert metas == [300, 450, 600, 800, 1200, 1600, 2000, 3000, 4000]
print("metas ok:", metas)
print("\nTUDO OK")
