# o selection é um método de organização
#  que procura o menor item de uma lista
#  e o salva em outra lista assim organizando-a

def menor_index(arr):

    menor = arr[0]
    index = 0

    for elemento in arr:

        if elemento < menor:
            menor = elemento
            index = arr.index(elemento)

    return index

def organizar(list):

    nova_lista = []

    tamanho = len(list) + 1

    for elemento in range(1, tamanho):

        index = menor_index(list)

        novo_valor = list.pop(index)

        nova_lista.append(novo_valor)

    return nova_lista

lista = [1, 7, 9, 2, 6, 0, 5, 3, 8, 4]

lista_nova = organizar(lista)

print(lista_nova)

