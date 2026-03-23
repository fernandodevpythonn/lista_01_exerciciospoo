from cachorro import cachorro
from gato import gato

somcachorro = cachorro()
somgato = gato()

def main():
    somcachorro.nome = input("nome do cachorro: ")
    somcachorro.som = input("som do animal: ")
    somcachorro.emitir_som()

    somgato.nome = input("nome do gato: ")
    somgato.som = input("nome do gato:")
    somgato.emitir_som()
if __name__ == "__main__":
    main()