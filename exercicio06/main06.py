from .emprestimo_livros.bibliotecario import bibliotecario
from .emprestimo_livros.livro import livro
biblioteca = bibliotecario()
livro = livro()
def menu():
  print("---Bibliotéca---")
  print("1 - Realizar empréstimo de livro")
  print("2 - Mostrar empréstimo")
  print("3 - Sair")
def main06():
  while True:
    menu()
    opcao = input("Faça sua escolha: ")
    print("")
    match opcao:
      case "1":
        livro.nome = input("Nome do livro: ")
        livro.autor = input("Autor do livro:")
        livro.material = input("Material do livro: ")
        livro.codigo = int(input("Código do livro: "))
        biblioteca.responsavel = input("Nome do responsável: ")
        biblioteca.data_emprestimo = input("Data de empréstimo: ")
        biblioteca.data_devolucao = input("Data de devolução: ")
      case "2":
        biblioteca.mostrar_emprestimo()
        livro.mostrar_livro()
        print(f"Livro: {livro.nome} emprestado para {biblioteca.responsavel}")
        print("")
