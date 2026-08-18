from estruturas import ListaEncadeada

# Remover da lista todas as copias de um certo elemento k

def remover_todas_copias(lista, k):
    if lista.head is None:
            return
    while lista.head is not None and lista.head.valor == k:
        lista.head = lista.head.next
    p = lista.head
    while p.next is not None:
        if p.next.valor == k:
            p.next = p.next.next
        else:
            p = p.next


lista = ListaEncadeada()
for valor in [1, 3, 3, 2, 3, 2]:
    lista.inserir_fim(valor)
remover_todas_copias(lista, 3)
lista.imprimir()

# COMO APENAS PERCORREMOS A LISTA E FAZEMOS MANIPULACOES QUE NAO CUSTAM GRANDE TEMPO DE EXECUCAO, A COMPLEXIDADE DO ALGORITIMO E O(n)