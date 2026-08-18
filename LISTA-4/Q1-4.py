from estruturas import ListaEncadeada

# Localizar o maior elemento da lista, e move-lo para a ultima posicao

def mover_maior_para_fim(lista):
    if lista.head is None or lista.head.next is None:
        return
    anterior_do_maior = None
    anterior = None
    maior = lista.head
    p = lista.head
    while p is not None:
        if p.valor > maior.valor:
            maior = p
            anterior_do_maior = anterior
        anterior = p
        p = p.next
    if maior.next is None:
        return
    if anterior_do_maior is None:
        lista.head = maior.next
    else:
        anterior_do_maior.next = maior.next
    anterior.next = maior
    maior.next = None


lista = ListaEncadeada()
for valor in [5, 8, 13, 2, 10]:
    lista.inserir_fim(valor)
mover_maior_para_fim(lista)
lista.imprimir()

# TEMPO DE EXECUCAO O(n) POIS TEMOS QUE PERCORRER O VETOR POR COMPLETO COM O PONTEIRO P