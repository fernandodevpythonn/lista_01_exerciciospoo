class produto:
  def __init__(self,produto_nome = "sem produto",produto_marca = "sem marca",produto_valor = "sem valor"):
    self.produto_valor = produto_valor
    self.produto_nome = produto_nome
    self.produto_marca = produto_marca
    self.lista_produtos = []

  def inserir_produtos(self,produto):
    self.lista_produtos.append(produto)

  def mostrar_produto(self):
    print(f"Nome: {self.produto_nome}")
    print(f"Valor: {self.produto_valor}")
    print(f"Marca: {self.produto_marca}")

  def listar_produtos(self):
    print("Produtos: ")
    for produto in self.lista_produtos:
      print(f"Produto: {produto}")