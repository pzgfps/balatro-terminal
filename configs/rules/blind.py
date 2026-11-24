from dataclasses import dataclass                               # mesma ideia da classe Carta: guarda dados sem precisar escrever o __init__
from configs.config import MAOS_INICIAIS, DESCARTES_INICIAIS    # constantes que ja existem no config.py

# este arquivo so tem logica (nada de print nem de tela): quem faz a tela so precisa chamar essas funcoes

METAS_BASE = [300, 800, 2000]       # meta base de cada rodada: a rodada 1 parte de 300, a 2 de 800 e a 3 de 2000
TIPOS_BLIND = [                     # cada rodada tem 3 blinds: (nome, multiplicador da meta, dinheiro de recompensa)
    ("Small", 1, 3),
    ("Big", 1.5, 4),
    ("Boss", 2, 5),                 # a Boss e so a blind mais dificil: meta maior, sem efeito especial
]

# ----------------------------------------------------Criar as blinds-----------------------------------------------------------#

@dataclass
class Blind:
    nome: str               # Small, Big ou Boss
    meta: int               # pontos que o jogador precisa fazer pra vencer a blind
    recompensa: int         # dinheiro ganho ao vencer

def total_de_rodadas():                 # quantas rodadas o jogo tem (uma por meta da lista METAS_BASE)
    return len(METAS_BASE)

def criar_blinds(rodada):               # rodada: 1, 2 ou 3 / devolve as 3 blinds dessa rodada, na ordem Small, Big, Boss
    base = METAS_BASE[rodada - 1]       # a lista comeca no 0, entao a rodada 1 e a posicao 0
    blinds = []                         # lista que vai guardar as 3 blinds
    for nome, multiplicador, recompensa in TIPOS_BLIND:     # repete uma vez pra cada tipo de blind
        meta = int(base * multiplicador)                    # int() tira a parte quebrada (300 x 1.5 = 450.0 vira 450)
        blinds.append(Blind(nome, meta, recompensa))
    return blinds

# ------------------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------Usar a blind na rodada----------------------------------------------------#

def iniciar_blind(estado):                          # prepara o estado pra comecar uma blind (estado: objeto do estado.py)
    estado.pontos = 0                               # a pontuacao zera a cada blind
    estado.fichas = 0
    estado.mult = 0
    estado.maos = MAOS_INICIAIS                     # volta pras 4 maos
    estado.descartes = DESCARTES_INICIAIS           # volta pros 3 descartes

def checar_rodada(estado, blind):                   # diz em que pe a blind esta: "vitoria", "derrota" ou "continua"
    if estado.pontos >= blind.meta:                 # bateu a meta: venceu (vem primeiro, pra a ultima mao poder ganhar)
        return "vitoria"
    if estado.maos <= 0:                            # nao bateu a meta e acabaram as maos: perdeu
        return "derrota"
    return "continua"

def finalizar_blind(estado, blind):                 # chamada depois da vitoria: paga a recompensa e devolve quanto o jogador ganhou
    ganho = blind.recompensa + estado.maos          # recompensa da blind + $1 por cada mao que sobrou
    estado.dinheiro += ganho
    return ganho

# ------------------------------------------------------------------------------------------------------------------------------#
