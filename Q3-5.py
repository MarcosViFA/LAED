from estruturas import ListaDuplamenteEncadeada

# Varredura e ordenação

def trocar_nos(lista, q):
    prox = q.next
    if prox is None:
        return q
    antes = q.prev
    depois = prox.next
    if antes is not None:
        antes.next = prox
    else:
        lista.head = prox
    prox.prev = antes
    prox.next = q
    q.prev = prox
    q.next = depois
    if depois is not None:
        depois.prev = q
    return prox


def uma_varredura(lista):
    houve_troca = False
    q = lista.head
    while q is not None and q.next is not None:
        if q.valor > q.next.valor:
            q = trocar_nos(lista, q)
            houve_troca = True
        q = q.next
    return houve_troca


def ordenar(lista):
    while uma_varredura(lista):
        pass


lista = ListaDuplamenteEncadeada()
for valor in [9, 3, 8, 5, 1]:
    lista.inserir_fim(valor)
ordenar(lista)
lista.imprimir()

# O TEMPO DE EXECUCAO DO ALGORITIMO NO PIOR CASO SAO NECESSARIAS ATE N VARREDURAS PARA ORDENAR COMPLETAMENTE A LISTA PORTANTO A COMPLEXIDADE E O(n^2)