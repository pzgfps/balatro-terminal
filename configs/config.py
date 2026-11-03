import shutil   # biblioteca para o preenchimento da borda no terminal  

# menu.py - art.py - 
cols, linhas = shutil.get_terminal_size()   # vai pegar o tamanho do terminal e jogar nas variáveis cols e linhas
ALTURA_BORDA = linhas - 3    # linhas pega o valor y (vertical)  -3 pra nao ultrapassar a borda
LARGURA_BORDA    = cols - 1    # cols pega o valor x (horizontal) -1 pra nao ultrapassar a borda
LARGURA_OPCAO = 30    # 
LARGURA_BOTAO = 25
ESPACO = 5

# art.py - 
LARGURA_MENU_LATERAL = 30    # largura do menu lateral (contando as duas bordas)

# menu.py - 
OPCOES_MENU = ["Continuar", "Novo Jogo", "Configurações"]   # lista constante para mostrar as opções da aba menu
OPCOES_CONFIG = ["Voltar", "Sair"]                          # lista constante para mostrar as opções da aba de configurações

VALORES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
NAIPES = ["ouros", "espadas", "copas", "paus"] 

# --- variaveis globais ---
TAMANHO_MAO = 8             # cartas na mão do jogador
MAX_JOGADAS = 5             # máximo de cartas por jogada
MAOS_INICIAIS = 4
DESCARTES_INICIAIS = 3
DINHEIRO_INICIAL = 4

# --- tamanho do desenho da carta ---
LARGURA_CARTA = 7
ALTURA_CARTA = 6

# --- teclas ---
SETA_ESQUERDA = 75
SETA_DIREITA = 77
ENTER = 13
