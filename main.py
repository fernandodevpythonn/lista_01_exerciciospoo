from modulos import *

def menu():
    print("2 - Exercício02")
    print("3 - Exercício03")
    print("4 - Exercício04")
    print("5 - Exercício05")
    print("6 - Exercício06")
    print("7 - Exercício07")
    print("8 - Exercício08")
    print("9 - Exercício09")
    print("10 - Exercício10")

def main():
    while True:
        menu()
        opcao = input("Escolha um exercício: ")
        match opcao:
            case "2":
                main02()
            case "3":
                main03()
            case "4":
                main04()
            case "5":
                main05()
            case "6":
                main06()
            case "7":
                pass
                # main07()
            case "8":
                main08()
            case "9":
                main09()
            case "10":
                main10()

if __name__ == "__main__":
    main()