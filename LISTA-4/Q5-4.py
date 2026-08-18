from estruturas import Node, ListaEncadeada

# Combinar os elementos das duas listas para produzir uma unica lista ordenada

def intercalar(lista1, lista2):
    resultado = ListaEncadeada()
    p1 = lista1.head
    p2 = lista2.head
    while p1 is not None and p2 is not None:
        if p1.valor <= p2.valor:
            resultado.inserir_fim(p1.valor)
            p1 = p1.next
        else:
            resultado.inserir_fim(p2.valor)
            p2 = p2.next
    while p1 is not None:
        resultado.inserir_fim(p1.valor)
        p1 = p1.next
    while p2 is not None:
        resultado.inserir_fim(p2.valor)
        p2 = p2.next
    return resultado


lista1 = ListaEncadeada()
for valor in [3, 6, 7, 10, 13]:
    lista1.inserir_fim(valor)
lista2 = ListaEncadeada()
for valor in [2, 4, 9, 11, 12]:
    lista2.inserir_fim(valor)
p = intercalar(lista1, lista2)
p.imprimir()

# TOMAND O TAMANHO DA LISTA1 COMO n E O TAMANHO DA LISTA2 COMO m  A COMPLEXIDADE DO ALGORITIMO SERA O((n+m)^2) POIS COMO TEMOS QUE PERCORRER OS 2 VETORES E INSERIR EM ORDEM EM UM NOVO
# (INSERIR NO FIM) TEREMOS A COMPLEXIDADE QUADRATICA.