
from info_estudante.estudante import estudante

estudante = estudante()

def menu():
  print("1 - cadastrar estudante ")
  print("2 - Dados do estudante")
  print("3 - Dados do curso")
  print("4 - Fechar")
def main():
  while True:
   menu()
   opcao = input("Escolha uma opção: ")
   match opcao:
     case "1":
       estudante.nome = input("Nome do aluno: ")
       estudante.idade = int(input("idade do aluno: "))
       estudante.matricula = int(input("Número de mátricula: "))
       estudante.nota = int(input("Nota do aluno: "))
       estudante.lista_notas.append(estudante.nota)
     case "2":
       estudante.mostrar_lista_notas()
       estudante.calculo_media()
if __name__ == "__main__":
  main()