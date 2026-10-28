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

