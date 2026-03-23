class produto:
  def __init__(self,nome = "sem nome",marca = "sem marca",valor = 0,produto = "sem produto"):
    self.nome = nome
    self.valor = valor
    self.marca = marca
    self.produto = produto
    self.lista_produtos = []
  def inserir_produtos(self):
    self.lista_produtos.append(self.produto)
    print(f"{produto}")
  def mostrar_produto(self):
    print(f"Nome: {self.nome}")
    print(f"Valor: {self.valor}")
    print(f"Marca: {self.marca}")
  def listar_produtos(self):
    print("Produtos: ")
    for produto in self.lista_produtos:
      print(produto)