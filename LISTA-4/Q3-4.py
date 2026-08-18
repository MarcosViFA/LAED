from estruturas import Node, ListaEncadeada

# Inverter a ordem dos elementos da lista

def inverter(lista):
    anterior = None
    atual = lista.head
    while atual is not None:
        proximo = atual.next
        atual.next = anterior
        anterior = atual
        atual = proximo
    lista.head = anterior


lista = ListaEncadeada()
for valor in [3, 2, 5, 9, 4]:
    lista.inserir_fim(valor)
inverter(lista)
lista.imprimir()

# TEMPO DE EXECUCAO O(n) POIS PERCORRE TODA A LISTA COM O PONTEIRO ATUAL NO WHILE