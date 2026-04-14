from .pedidos.cliente_info import cliente
from .pedidos.pedido_info import pedido
cli = cliente()
ped = pedido()
import random
def menu():
    print("------Pedido------\n")
    print("1 - Adicionar cliente")
    print("2 - Adicionar pedido")
    print("3 - Dados de cliente")
    print("4 - Dados do pedido")
    print("5 - Sair")

def main10():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                cli.nome = input("Nome do cliente: ")
                cli.cpf = int(input("CPF do Cliente: "))
                print("---endereço---")
                cidade = input("cidade: ")
                bairro = input("bairro: ")
                rua = input("rua: ")
                numero = int(input("Número: "))
                cli.adicionar_endereco(cidade,bairro,rua,numero)
            case "2":
                ped.produto = input("Produto: ")
                ped.status = random.choice(['Entregue','em transito','em desembarque','enviado'])
                ped.numero_pedido = random.random()
                cidade = input("cidade: ")
                bairro = input("bairro: ")
                rua = input("rua: ")
                numero = int(input("número: "))
                ped.adicionar_endereco(cidade,bairro,rua,numero)
                ped.mostrar_endereco()
                ped.mostrar_pedido()
            case "3":
                cli.mostrar_cliente()
                cli.mostrar_endereco()
            case "4":
                ped.mostrar_pedido()
