from estruturas import Node, ListaEncadeada

# duplicar os impares

def duplicar_impares(lista):
    p = lista.head
    while p is not None:
        if p.valor % 2 != 0:
            novo_no = Node(p.valor)
            novo_no.next = p.next
            p.next = novo_no
            p = novo_no.next
        else:
            p = p.next


lista = ListaEncadeada()
for valor in [2, 7, 6, 3]:
    lista.inserir_fim(valor)
duplicar_impares(lista)
lista.imprimir()

# TEMPO DE EXECUCAO O(n) POIS PERCORRE TODA A LISTA COM O PONTEIRO p E A CONDICAO SE FOR IMPAR OU PAR E O(1) OU SEJA NAO INTERFERE NA COMPLEXIDADE