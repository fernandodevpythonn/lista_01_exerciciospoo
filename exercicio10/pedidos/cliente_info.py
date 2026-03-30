class cliente:
    def __init__(self, nome = "sem nome",cpf = 0,cidade = "sem cidade", bairro = "sem bairro", rua = "sem bairro", numero = 0 ):
      self.nome = nome
      self.cpf = cpf
      self.endereco = {
      "cidade": cidade,
      "bairro": bairro,
      "rua": rua,
      "numero": numero
      }
  
    def mostrar_cliente(self):
      print(self.nome)
      print(self.cpf)
    def adicionar_endereco(self,cidade,bairro,rua,numero):
      self.endereco["cidade"] = cidade
      self.endereco["bairro"] = bairro
      self.endereco["rua"] = rua
      self.endereco["numero"] = numero
    
    def mostrar_endereco(self):
      for chave,valor in self.endereco.items():
        print(f"{chave}: {valor}")