

def lerArq ():
    with open("problema1.txt", 'r') as arquivo:
        restricoes = arquivo.readline()
        restricoes = [restricoes.split()]
        for x in restricoes:
            int(x)
        print(restricoes)



def opcao1():#função para fim de teste
    lerArq()

def opcao2():#função para fim de testeaaa
    print("Você escolheu a Opção 2")

def main():#Menu
    while True:
        print("\nMenu:")
        print("1. Executar Symplex intermediário.")
        print("2. Executar Symplex final.")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            opcao1()
        elif escolha == '2':
            opcao2()
        elif escolha == '3':
            print("Tchau Tchau Renato André")
            break
        else:
            print("Opção inválida. Digite novamente professor.")

if __name__ == "__main__":
    main()