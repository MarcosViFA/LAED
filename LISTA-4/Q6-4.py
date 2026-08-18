from estruturas import Node, ListaEncadeada

# Particao dado um k

def particionar(lista, k):
    menores_iguais = ListaEncadeada()
    maiores = ListaEncadeada()
    p = lista.head
    while p is not None:
        if p.valor <= k:
            menores_iguais.inserir_fim(p.valor)
        else:
            maiores.inserir_fim(p.valor)
        p = p.next
    if menores_iguais.head is None:
        lista.head = maiores.head
    else:
        lista.head = menores_iguais.head
        p = menores_iguais.head
        while p.next is not None:
            p = p.next
        p.next = maiores.head


lista = ListaEncadeada()
for valor in [9, 2, 5, 6, 1]:
    lista.inserir_fim(valor)
particionar(lista, 6)
lista.imprimir()

# NO PIOR CASO O TEMPO DE EXECUCAO E O(n^2) POIS PRECISAMOS PRESERVAR A ORDEM DA LISTA NO PARTICIONAMENTO (INSERIR NO FIM), LOGO TEREMOS 2 LACOS CONCATENADOS