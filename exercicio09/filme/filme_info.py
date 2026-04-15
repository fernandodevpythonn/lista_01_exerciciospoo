from .categorias_info import categorias

cat = categorias()
cat = categorias
class filmes:
    def __init__(self,nome = "sem nome",ano_lancamento = 0,criador = "sem criador",categoria = "sem categoria"):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.criador = criador
        self.categoria = categoria
    def mostrar_filme(self):
        print(self.nome)
        print(self.ano_lancamento)
        print(self.criador)
        print(self.categoria)
