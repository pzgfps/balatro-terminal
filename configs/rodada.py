from dataclasses import dataclass, field                        # field cria listas novas pra cada Partida (nao compartilhadas)
from configs.config import TAMANHO_MAO                          # constante que ja existe no config.py
from configs.estado import Estado
from configs.rules.baralho import criar_baralho, comprar_cartas
from configs.rules.blind import criar_blinds, total_de_rodadas, iniciar_blind, checar_rodada, finalizar_blind
from configs.mao import descartar_cartas, jogar_cartas
from configs.pontuacao import pontuar_jogada

# este arquivo so tem logica (nada de print nem de tela): quem faz a tela so precisa chamar essas funcoes
#
# como o jogo anda (o campo "status" da Partida diz em qual passo ele esta):
#   "jogando"       -> o jogador joga e descarta cartas
#   "vitoria_blind" -> bateu a meta: a tela mostra a vitoria e chama fechar_blind()
#   "loja"          -> blind paga: a tela abre a loja e depois chama iniciar_blind_atual()
#   "derrota"       -> acabaram as maos sem bater a meta: fim de jogo
#   "fim_vitoria"   -> venceu todas as blinds de todas as rodadas: fim de jogo

# ----------------------------------------------------Criar a partida-----------------------------------------------------------#

@dataclass
class Partida:                                          # guarda tudo que muda durante o jogo num lugar so
    estado: Estado                                      # pontos, maos, descartes e dinheiro (o menu lateral le daqui)
    rodada: int = 1                                     # rodada atual (1, 2 ou 3)
    posicao_blind: int = 0                              # 0 = Small, 1 = Big, 2 = Boss
    blinds: list = field(default_factory=list)          # as 3 blinds da rodada atual
    baralho: list = field(default_factory=list)
    mao: list = field(default_factory=list)             # as cartas na mao do jogador
    selecionadas: list = field(default_factory=list)    # posicoes das cartas marcadas
    coringas: list = field(default_factory=list)        # coringas que o jogador tem
    status: str = "loja"                                # comeca "pronta pra iniciar a blind"

def criar_partida():                                    # monta uma partida nova (serve tambem pra reiniciar o jogo)
    partida = Partida(Estado())                         # estado novo: 4 maos, 3 descartes e o dinheiro inicial
    partida.blinds = criar_blinds(partida.rodada)       # as 3 blinds da rodada 1
    return partida

def blind_atual(partida):                               # devolve a blind que esta valendo agora
    return partida.blinds[partida.posicao_blind]

# ------------------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------Jogar uma blind-----------------------------------------------------------#

def iniciar_blind_atual(partida):                       # prepara a blind: zera o estado, embaralha e compra a mao
    iniciar_blind(partida.estado)                       # pontos 0, 4 maos e 3 descartes
    partida.baralho = criar_baralho()                   # baralho novo e embaralhado a cada blind
    partida.mao = []
    comprar_cartas(partida.mao, partida.baralho, TAMANHO_MAO)
    partida.selecionadas = []
    partida.status = "jogando"

def jogar_mao(partida):                                 # joga as cartas marcadas / devolve (nome da mao, pontos) ou None se nada foi jogado
    if partida.status != "jogando":                     # so da pra jogar enquanto a blind esta rolando
        return None
    cartas = jogar_cartas(partida.mao, partida.selecionadas, partida.baralho, partida.estado)
    if len(cartas) == 0:                                # nenhuma carta marcada (ou sem maos): nao jogou
        return None
    nome, pontos = pontuar_jogada(partida.estado, cartas, partida.coringas)
    resultado = checar_rodada(partida.estado, blind_atual(partida))     # "vitoria", "derrota" ou "continua"
    if resultado == "vitoria":
        partida.status = "vitoria_blind"
    elif resultado == "derrota":
        partida.status = "derrota"
    return nome, pontos

def descartar_mao(partida):                             # descarta as cartas marcadas / devolve quantas cartas foram descartadas
    if partida.status != "jogando":
        return 0
    descartadas = descartar_cartas(partida.mao, partida.selecionadas, partida.baralho, partida.estado)
    return len(descartadas)

def fechar_blind(partida):                              # depois da vitoria: paga a recompensa e avanca / devolve quanto dinheiro ganhou
    if partida.status != "vitoria_blind":               # so fecha uma blind que foi vencida
        return 0
    ganho = finalizar_blind(partida.estado, blind_atual(partida))
    partida.posicao_blind += 1                          # vai pra proxima blind (Small -> Big -> Boss)
    if partida.posicao_blind >= len(partida.blinds):    # acabaram as 3 blinds dessa rodada
        partida.rodada += 1
        partida.posicao_blind = 0
        if partida.rodada > total_de_rodadas():         # acabaram todas as rodadas: o jogador venceu o jogo
            partida.status = "fim_vitoria"
            return ganho
        partida.blinds = criar_blinds(partida.rodada)   # monta as blinds da proxima rodada
    partida.status = "loja"                             # a tela abre a loja e depois chama iniciar_blind_atual()
    return ganho

def jogo_acabou(partida):                               # True quando nao da mais pra jogar (derrota ou vitoria final)
    return partida.status == "derrota" or partida.status == "fim_vitoria"

# ------------------------------------------------------------------------------------------------------------------------------#
