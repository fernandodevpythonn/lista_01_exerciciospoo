from conta import conta_bancaria

conta = conta_bancaria()

def menu():
    print("1 - Adicionar titular")
    print("2 - Depositar")
    print("3 - Saque")
    print("4 - Verificar saldo")
    print("5 - Histórico de saques")
    print("6 - Histórico de depositos")
    print("7 - fechar")

def main():
    while True:
     menu()
     opcao = input("Escolha uma opção: ")
     match opcao:
        case "1":
           conta.titular = input("nome do títular: ")
           if conta.titular.isalpha():
            print(f"{conta.titular} cadastrado")
           else:
            raise ValueError("Erro, digite um nome válido")
        case "2":
           try:
            deposito = float(input("digite um valor: "))
            conta.inserir_deposito(deposito)
            conta.historico_deposito.append(deposito)
            conta.saldo += deposito
           except ValueError:
            print("Erro ao fazer o deposito, digite um valor float")
        case "4":
         print(f"Títular: {conta.titular}")
         print(f"Saldo = {conta.saldo}")
        case "3":
         try:
           conta.saque = int(input("Digite um valor"))
           conta.saldo -= conta.saque
           conta.historico_saque.append(conta.saque)
           print(f"Títular: {conta.titular}")
           print(f"Saldo Atual: {conta.saldo}")
         except ValueError:
           print("Erro: Digite um valor float")
        case "5":
         conta.mostrar_historico_saque()
        case "6":
         conta.mostrar_historico_deposito()
        case "7":
         print("Sistema fechado")
         break
if __name__ == "__main__":
  main()