# Recursão é o processo de transformar uma tarefa complexa em uma
# tarefa simples repetidas vezes até chegar em um caso base fácil
# de resolver, porém consumindo muita memória.
# aqui irei fazer alguns exercícios feitos no livro "Entendendo
# Algoritmos" do capítulo Quicksort

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        valor = lista.pop(0)
        resultado = valor + soma(lista)
    return resultado

lista = [1, 2, 3, 4, 5]

print(soma(lista))
