class gato:
    def __init__(self,nome = "sem nome",som = "sem som"):
        self.nome = nome
        self.som = som
        
    def emitir_som(self):
        print(f"Som: {self.som}")