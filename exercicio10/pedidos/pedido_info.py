from .cliente_info import cliente
cli = cliente()

class pedido:
    def __init__(self, produto = "sem produto", status = "sem status", numero_pedido = 0,cidade = "sem cidade", bairro = "sem bairro",rua = "sem rua", numero = 0):
        self.produto = produto
        self.status = status
        self.numero_pedido = numero_pedido
        self.endereco_saida = {
        "cidade": cidade,
        "bairro": bairro,
        "rua": rua,
        "numero": numero
        }
  
    def adicionar_endereco(self,cidade,bairro,rua,numero):
      self.endereco_saida["cidade"] = cidade
      self.endereco_saida["bairro"] = bairro
      self.endereco_saida["rua"] = rua
      self.endereco_saida["numero"] = numero

    def mostrar_pedido(self):
       print(f"Produto: {self.produto}")
       print(f"Status: {self.status}")
       print(f"Número de pedido: {self.numero_pedido}")
       print("Cliente: ")
       print(cli.nome)
       print("Destino: ")
       print(cli.mostrar_endereco)
       print("Saída: ")
       self.mostrar_endereco()
    def mostrar_endereco(self):
       for chave, valor in self.endereco_saida.items():
          print(f"{chave}:{valor}")