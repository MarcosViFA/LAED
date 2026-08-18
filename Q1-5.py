from estruturas import ListaDuplamenteEncadeada

# Imprimir o elemento central da lista

def elemento_central(lista):
    n = 0
    p = lista.head
    while p is not None:
        n += 1
        p = p.next
    if n == 0:
        return None
    posicao_central = (n - 1) // 2
    p = lista.head
    for i in range(posicao_central):
        p = p.next

    return p.valor


lista = ListaDuplamenteEncadeada()
for valor in [3, 9, 5, 2, 8]:
    lista.inserir_fim(valor)
print(elemento_central(lista))

# O TEMPO DE EXECUCAO E O(n) POIS TEMOS QUE PERCORRER TODA A LISTA PARA SABERMOS O INDICE DO ELEMENTO CENTRAL.