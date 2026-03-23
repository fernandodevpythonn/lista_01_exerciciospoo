from cliente_produto.cliente import cliente
from cliente_produto.produto import produto
prod = produto()
cliente = cliente()


def menu():
 print("1 - Cadastrar cliente")
 print("2 - Dados do cliente")
 print("3 - Cadastrar produto")
 print("4 - Produtos cadastrados")
 print("5 - Realizar compra")
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
      input("aperte enter para voltar")

    case "3":
      prod.nome = input("Nome do produto: ")
      prod.marca = input("Marca: ")
      prod.valor = float(input("Valor: "))
      prod.produto += prod.nome
      prod.produto += prod.marca
      print(prod.produto)
      print(prod.lista_produtos)
      input("aperte enter para voltar")

    case "4":
      prod.listar_produtos()
      input("aperte enter para voltar")

    case "5":
      if cliente.nome == True:
        nome = input("digite o nome do produto: ")
        marca = input("marca: ")
        if nome == produto.nome and marca == prod.marca:
          print("produto existe")
          print(f"Produto: {produto.nome} Valor: {prod.valor}")
          comprar = input("deseja finalizar a compra? ")
          if comprar == "sim":
              print("="*30)
              print(f"Produto {nome} enviado para {cliente.nome}\n no endereço: ")
              cliente.mostrar_endereco()
              input("Digite enter para volta: ")
          else:
           print("fim")
        else:
          print("produto não existe")
      else:
        print("cliente ainda não cadastrado")
        input("aperte enter para voltar")

if __name__ == "__main__":
  main()