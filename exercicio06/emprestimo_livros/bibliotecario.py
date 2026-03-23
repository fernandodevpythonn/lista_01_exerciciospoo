class bibliotecario:
  def __init__(self,data_emprestimo = 0,data_devolucao = 0,responsavel = "sem nome"):
    self.data_emprestimo = data_emprestimo
    self.data_devolucao = data_devolucao
    self.responsavel = responsavel
  def mostrar_emprestimo(self):
    print(f"data empréstimo: {self.data_emprestimo}")
    print(f"data devolução: {self.data_devolucao}")
    print(f"responsável: {self.responsavel}")
    print("")