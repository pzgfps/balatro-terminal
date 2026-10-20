from interface.menu import menu, configuracoes


def main():
    while True:
        opcao = menu()
        if opcao == 0:
            print("Você escolheu continuar o jogo")      # testar se a opção está indo certa
            break   # continuar jogo
        elif opcao == 1:

            print("Você escolheu iniciar um novo jogo")  # testar se a opção está indo certa
            break   # novo jogo
        elif opcao == 2:
            if configuracoes() == 1:
                print("Você escolheu fechar o jogo, até mais!")
                break    

if __name__ == "__main__":      # comentario atoa
    main()