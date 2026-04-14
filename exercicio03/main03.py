from .carro import carro_a

def main03():
    carro_antigo = carro_a()
    carro_antigo.marca = input("marca do carro: ")
    carro_antigo.cor = input("cor do carro: ")
    if carro_antigo.marca.isalpha() and carro_antigo.cor.isalpha():
     try:
      carro_antigo.ano = int(input("ano do carro: "))
     except ValueError:
        print("Erro; Digite um ano válido")
     cor_nova = input("Nova cor: ")
     marca_nova = input("nova marca: ")
     if cor_nova.isalpha() and marca_nova.isalpha():
      carro_antigo.atualizar_cor(cor_nova)
      carro_antigo.atualizar_marca(marca_nova)
     else:
       raise ValueError("Erro: Digite um valor válido")
    else:
      raise ValueError("Erro: Digite um valor válido")
