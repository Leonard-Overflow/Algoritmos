lista = [2, 3, 1, 7, 4, 9, 8, 0, 6, 5]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    tamanho = round(len(lista)/2)
    pivo = lista[tamanho]
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort(lista))