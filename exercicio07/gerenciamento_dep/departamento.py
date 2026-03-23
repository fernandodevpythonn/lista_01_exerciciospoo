class funcionario:
  def __init__(self,nome = "sem nome",cargo = "sem cargo"):
    self.nome = nome
    self.cargo = cargo
    self.salario = []
  def mostrar_funcionario(self):
    print(f"Nome: {self.nome}")
    print(f"Cargo: {self.cargo}")
    print(f"Salário: {self.salario}")
class departamento:
  def __init__(self,):
    empresa = "Ativa_agência"
