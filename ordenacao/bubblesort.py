# O bubble sort é um método de organização que
# percorre toda a lista de n elementos n
# vezes verificando quais são maiores e
# quais são menores e organizando-os

def bubblesort(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        for j in range(tamanho - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

lista = [19, 5, 28, 12, 1, 22, 9, 30, 15, 6, 2, 24, 17, 29, 8, 21, 13, 27, 3, 10, 25, 14, 23, 7, 26, 11, 4, 18, 20, 16]

print(bubblesort(lista))