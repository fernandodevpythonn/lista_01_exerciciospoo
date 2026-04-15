from .cliente_produto.cliente import cliente
from .cliente_produto.produto import produto
prod = produto()
cli = cliente()


def menu():
 print("1 - Cadastrar cliente")
 print("2 - Dados do cliente")
 print("3 - Cadastrar produto")
 print("4 - Produtos cadastrados")
 print("5 - Realizar compra")
def main08():
 while True:
  menu()
  opcao = input("Escolha uma opção: ")
  match opcao:

    case "1":
      cli.nome = input("Nome: ")
      try:
       cli.cpf = int(input("cpf: "))
      except ValueError:
        print("erro: valor inválido")
      cidade = input("Cidade: ")
      bairro = input("Bairro: ")
      rua = input("Rua: ")
      try:
        numero = int(input("Número: "))
      except ValueError:
        print("Erro: Digite um número válido")
      cli.adicionar_endereco(cidade,bairro,rua,numero)
      cli.mostrar_endereco()
      print("=====")

    case "2":
      cli.mostrar_cliente()
      input("aperte enter para voltar")

    case "3":
      prod.produto_nome = input("Nome do produto: ")
      prod.produto_marca = input("Marca: ")
      try:
       prod.produto_valor = float(input("Valor: "))
      except ValueError:
        print("erro: valor inválido")
      prod.inserir_produtos(prod.produto_nome)
      input("aperte enter para voltar")

    case "4":
      prod.listar_produtos()
      input("aperte enter para voltar")

    case "5":
      if cli.nome:
        if prod.produto_nome:
          nome = input("digite o nome do produto: ")
          marca = input("marca: ")
          if nome in prod.lista_produtos and marca in prod.lista_produtos:
            print("produto existe")
            print(f"Produto: {prod.produto_nome} Valor: {prod.produto_valor}")
            comprar = input("deseja finalizar a compra? ")
            if comprar == "sim":
              print("="*30)
              print(f"Produto {nome} enviado para {cli.nome}\n no endereço: ")
              cli.mostrar_endereco()
              input("Digite enter para volta: ")
            else:
             print("fim")
          else:
           print("produto não existe")
        else:
          print("Erro: Produto não cadastrado")
          input("aperte enter para voltar")
      else:
        print("cliente ainda não cadastrado")
        input("aperte enter para voltar")
