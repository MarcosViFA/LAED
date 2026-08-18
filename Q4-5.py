from estruturas import ListaDuplamenteEncadeada

# Partição

def particionar(lista, k):
    if lista.head is None:
        return
    q = lista.head
    r = lista.head
    while r.next is not None:
        r = r.next
    while True:
        while q is not r and q.valor <= k:
            q = q.next
        while q is not r and r.valor > k:
            r = r.prev
        if q is r:
            break
        q.valor, r.valor = r.valor, q.valor
        q = q.next
        if q is r:
            break
        r = r.prev


lista = ListaDuplamenteEncadeada()
for valor in [9, 2, 5, 6, 1]:
    lista.inserir_fim(valor)
particionar(lista, 5)
lista.imprimir()

# MESMO COM OS DOIS PONTEIROS PERCORRENDO A LISTA EM DIRECOES OPOSTAS COMO ELES PARAM QUANDO SE ENCONTRAR A COMPLEXIDADE DO ALGORITIMO E O(n).