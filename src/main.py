import sys, os  # aparentemente isso aqui arruma o erro que estava dando por causa dos imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # aparentemente isso aqui arruma o erro que estava dando por causa dos imports
import WConio2 as W
from assets.art.menu import menu_inicial, menu_configuracoes    # chamando as funcoes do menu
from assets.art.art import desenhar_menu_lateral, borda                # chamando a funcao de menu_lateral
from configs.estado import Estado                               # chamando o objeto estado para a visualização dos dados

estado = Estado()

def main():
    while True:
        opcao = menu_inicial()
        if opcao == 0:
            print("Você escolheu continuar o jogo")      # testar se a opção está indo certa
            break   # continuar jogo
        elif opcao == 1:
            W.clrscr()
            borda()         # manter aqui enquanto nao temos a funcao
            desenhar_menu_lateral(10, 2, estado)
            #print("Você escolheu iniciar um novo jogo")  # testar se a opção está indo certa
            break   
        elif opcao == 2:
            if menu_configuracoes() == 1:
                W.clrscr()
                print("Você escolheu fechar o jogo, até mais!")
                break    

if __name__ == "__main__":      
    main()