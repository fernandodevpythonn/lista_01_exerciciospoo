class carro_a:
    def __init__(self,marca = "sem marca", cor = "sem cor", ano = 0):
        self.marca = marca
        self.cor = cor
        self.ano = ano
    def atualizar_marca(self,nova_marca):
        self.marca = nova_marca
        print(f"Nova marca: {nova_marca}")
    def atualizar_cor(self,nova_cor):
        self.cor = nova_cor
        print(f"Nova cor: {nova_cor}")