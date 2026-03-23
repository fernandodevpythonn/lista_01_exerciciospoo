class estudante:
    def __init__(self,nota = 0,nome="sem nome",idade = 0,matricula = 0,media = 0):
        self.nome = nome
        self.lista_notas = []
        self.idade = idade
        self.nota = nota
        self.media = media
        self.matricula = matricula
    def cadastrar_notas(self,nota):
        self.lista_notas.append(nota)
    def mostrar_lista_notas(self):
        for nota in self.lista_notas:
            print(f"Notas {nota}")
    def calculo_media(self):
        self.media = sum(self.lista_notas) / len(self.lista_notas)
        print(self.media)