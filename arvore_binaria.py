from math import floor
from quicksort import quicksort
from quicksort import lista

def arvore_binaria(lista, item):
    baixo = lista[0]
    alto = len(lista) - 1

    while baixo <= alto:

        meio = floor((baixo + alto) / 2)

        if meio == item:
            return f"O valor do item é {item}" # Eu acho que é isso
        elif meio < item:
            baixo = meio + 1
        else:
            alto = meio - 1

    print("O valor do item não existe na lista")

lista_sort = quicksort(lista)
resultado = arvore_binaria(lista_sort, 18)
print(resultado)

