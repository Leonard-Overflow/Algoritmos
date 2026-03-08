# uma árvore binária é um método de busca
# onde a lista de n elementos é dividida
# e verificndo se o meio da lista é é menor,
# igual ou menor que o item procurado

from math import floor
from bubblesort import bubblesort
from bubblesort import lista

def arvore_binaria(lista, item):
    baixo = lista[0]
    alto = len(lista) - 1

    while baixo <= alto:

        meio = floor((baixo + alto) / 2)

        if meio == item:
            return f"O valor do item é {item}"
        elif meio < item:
            baixo = meio + 1
        else:
            alto = meio - 1

    print("O valor do item não existe na lista")

lista_sort = bubblesort(lista)
resultado = arvore_binaria(lista_sort, 18)
print(resultado)

