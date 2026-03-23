class produto:
  def __init__(self,nome = "sem nome",valor = 0):
    self.nome = nome
    self.valor = valor
  def mostrar_produto(self):
    print(f"Nome: {self.nome}")
    print(f"Valor: {self.valor}")