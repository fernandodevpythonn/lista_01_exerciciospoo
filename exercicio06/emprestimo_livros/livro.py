class livro:
  def __init__(self,nome = "sem nome", autor = "autor",codigo = 0,material = "sem material"):
    self.nome = nome
    self.autor = autor
    self.material = material
    self.codigo = codigo
  def mostrar_livro(self):
    print(f"Livro: {self.nome}")
    print(f"autor: {self.autor}")
    print(f"codigo: {self.codigo}")
    print(f"Material: {self.material}")
    