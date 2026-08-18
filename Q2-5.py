from estruturas import ListaDuplamenteEncadeada

# Operação de atualização

def atualizar(lista, x, y):
    p = lista.head
    while p is not None and p.valor != x:
        p = p.next
    if p is None:
        return
    if p.prev is not None:
        p.prev.next = p.next
    else:
        lista.head = p.next
    if p.next is not None:
        p.next.prev = p.prev
    p.valor = y
    p.prev = None
    p.next = None
    if lista.head is None or y <= lista.head.valor:
        p.next = lista.head
        if lista.head is not None:
            lista.head.prev = p
        lista.head = p
        return
    atual = lista.head
    while atual.next is not None and atual.next.valor < y:
        atual = atual.next
    p.next = atual.next
    p.prev = atual
    if atual.next is not None:
        atual.next.prev = p
    atual.next = p


lista = ListaDuplamenteEncadeada()
for valor in [3, 5, 9, 10, 15]:
    lista.inserir_fim(valor)
atualizar(lista, 5, 11)
lista.imprimir()

# NO PIOR CASO O TEMPO DE EXECUCAO DESSE ALGORITIMO E O(n) POIS TERIAMOS QUE PERCORRER TODA A LISTA PARA ENCONTRAR E DEPOIS INSERIOR O NOVO.