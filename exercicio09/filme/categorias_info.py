class categorias:
    def __init__(self,nome = "sem nome"):
        self.nome = nome
        self.categorias = []
    def inserir_categoria(self,cat):
        self.categorias.append(cat)
    def mostrar_categorias(self):
        print(", ".join(self.categorias))
        print("")