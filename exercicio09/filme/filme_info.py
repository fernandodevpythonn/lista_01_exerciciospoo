
class filmes:
    def __init__(self,nome = "sem nome",ano_lancamento = 0,criador = "sem criador"):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.criador = criador
    def mostrar_filme(self):
        print(self.nome)
        print(self.ano_lancamento)
        print(self.criador)