from filme.filme_info import filmes
from filme.categorias_info import categorias
filme = filmes()
cat = categorias()
def menu():
    print("============= Filmes ===========")
    print("1 - cadastrar categoria")
    print("2 - Adicionar filme")
    print("3 - Mostrar filme")
    print("4 - Mostrar categorias")
    print("5 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                cat.nome = input("Nome da categoria: ")
                cat.inserir_categoria(cat.nome)
            case "2":
                filme.nome = input("Nome do filme: ")
                filme.ano_lancamento = int(input("ano de lançamento do filme: "))
                filme.criador = input("Nome do autor(a): ")
                print(cat.categorias)
                filme.categoria = input("Qual categoria deseja inserir? ")
                if filme.categoria in cat.categorias:
                  filme.categoria = filme.categoria
                else:
                    print("Categoria não existe")
            case "3":
                filme.mostrar_filme()
            case "4":
                print("----Categorias----- ")
                cat.mostrar_categorias()
    
if __name__ == "__main__":
    main()