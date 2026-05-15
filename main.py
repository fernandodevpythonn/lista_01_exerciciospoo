from modulos import *

def menu():
    print("LISTA DE EXERCÍCIOS")
    print("2 - Exercício02")
    print("3 - Exercício03")
    print("4 - Exercício04")
    print("5 - Exercício05")
    print("6 - Exercício06")
    print("7 - Exercício07")
    print("8 - Exercício08")
    print("9 - Exercício09")
    print("10 - Exercício10")
    print("0 - Fechar sistema")

def main():
    while True:
        menu()
        opcao = input("Escolha um exercício: ")
        match opcao:
            case "2":
                main02()
                input("Aperte Enter para voltar")
                
            case "3":
                main03()
                input("Aperte Enter para voltar")

            case "4":
                main04()
                input("Aperte Enter para voltar")

            case "5":
                main05()
                input("Aperte Enter para voltar")

            case "6":
                main06()
                input("Aperte Enter para voltar")

            case "7":
                pass
                # main07()
                input("Aperte Enter para voltar")

            case "8":
                main08()
                input("Aperte Enter para voltar")

            case "9":
                main09()
                input("Aperte Enter para voltar")

            case "10":
                main10()
                input("Aperte Enter para voltar")

            case "0":
                print("Sistema fechado")
                break

if __name__ == "__main__":
    main()