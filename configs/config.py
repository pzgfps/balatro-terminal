import shutil   # biblioteca para o preenchimento da borda no terminal  

cols, linhas = shutil.get_terminal_size()   # vai pegar o tamanho do terminal e jogar nas variáveis cols e linhas
ALTURA = linhas - 3    # linhas pega o valor y (vertical)  -3 pra nao ultrapassar a borda
LARGURA = cols - 1    # cols pega o valor x (horizontal) -1 pra nao ultrapassar a borda

OPCOES_MENU = ["Continuar", "Novo Jogo", "Configurações"]   # lista constante para mostrar as opções da aba menu
OPCOES_CONFIG = ["Voltar", "Sair"]                          # lista constante para mostrar as opções da aba de configurações

LARGURA_OPCAO = 30