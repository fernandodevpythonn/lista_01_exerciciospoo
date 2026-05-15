
from .info_estudante.estudante import estudante

estudante = estudante()

def menu():
  print("1 - cadastrar estudante ")
  print("2 - Dados do estudante")
  print("3 - Fechar")
def main05():
  while True:
   menu()
   opcao = input("Escolha uma opção: ")
   match opcao:
     case "1":
       estudante.nome = input("Nome do aluno: ")
       try:
        estudante.idade = int(input("idade do aluno: "))
       except ValueError:
         print("erro: valor inválido")
       estudante.matricula = int(input("Número de mátricula: "))
       try:
         estudante.nota = int(input("Nota do aluno: "))
         estudante.lista_notas.append(estudante.nota)
       except ValueError:
         print("erro: valor inválido")
     case "2":
       estudante.mostrar_lista_notas()
       estudante.calculo_media()
     case "3":
       print("sistema fechado")
       break