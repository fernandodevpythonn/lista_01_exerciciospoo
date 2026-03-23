from cliente_produto.cliente import cliente
cliente = cliente()
def menu():
 print("1 - Cadastrar cliente")
 print("2 - Dados do cliente")
def main():
 while True:
  menu()
  opcao = input("Escolha uma opção: ")
  match opcao:
    case "1":
      cliente.nome = input("Nome: ")
      cliente.cpf = int(input("cpf: "))
      cidade = input("Cidade: ")
      bairro = input("Bairro: ")
      rua = input("Rua: ")
      try:
        numero = int(input("Número: "))
      except ValueError:
        print("Erro: Digite um número válido")
      cliente.adicionar_endereco(cidade,bairro,rua,numero)
      cliente.mostrar_endereco()
      print("=====")
    case "2":
      cliente.mostrar_cliente()
      print("======")
main()