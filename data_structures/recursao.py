# Recursão é o processo de transformar uma tarefa complexa em uma
# tarefa simples repetidas vezes até chegar em um caso base fácil
# de resolver, porém consumindo muita memória.
# aqui irei fazer alguns exercícios feitos no livro "Entendendo
# Algoritmos" do capítulo Quicksort

lista = [1, 2, 3, 4, 5, 6, 10]

# Exercício 1 proposto no livro
# 4.1 Escreva o código para a função soma, vista anteriormente.

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        valor = lista.pop(0)
        resultado = valor + soma(lista)
    return resultado

# Exercício 2 proposto no livro
#4.2 Escreva uma função recursiva que conte o número de itens em uma lista.

def contar(lista):
    contador = 0
    if lista != []:
        lista.remove(lista[0])
        contador += 1
    else:
        return contador
    contador += contar(lista)
    return contador

# Exercício 3 proposto no livro
# 4.3 Encontre o valor mais alto em uma lista.

def maior_valor(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento

    return maior

"""
Exercício 3 proposto no livro
4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um
algoritmo do tipo dividir para conquistar. Você consegue determinar o
caso-base e o caso recursivo para a pesquisa binária?

Em uma árvore binária o caso base será o momento em que o meio é igual 
ao item procurado e o caso recursivo é quando a pesquisa repete após 
verificar que o item em questãoé maior ou menor que o meio. 
"""