def quicksort(lista):
    tamanho = len(lista)

    for i in range(tamanho):

        for i in range(tamanho - 1):

            if lista[i + 1] in lista:
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]

lista = [19, 5, 28, 12, 1, 22, 9, 30, 15, 6, 2, 24, 17, 29, 8, 21, 13, 27, 3, 10, 25, 14, 23, 7, 26, 11, 4, 18, 20, 16]


