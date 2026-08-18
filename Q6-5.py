from estruturas import ListaDuplamenteEncadeada

# Operações sobre vetores esparsos

def busca_por_indice(lista, k):
    p = lista.head
    while p is not None:
        posicao, valor = p.valor
        if posicao == k:
            return valor
        p = p.next
    return 0


def busca_por_valor(lista, x):
    p = lista.head
    while p is not None:
        posicao, valor = p.valor
        if valor == x:
            return posicao
        p = p.next
    return -1


def atualizacao(lista, x, k):
    p = lista.head
    while p is not None:
        posicao, valor = p.valor
        if posicao == k:
            if x == 0:
                # remove o no (vetor esparso não guarda zeros)
                if p.prev is not None:
                    p.prev.next = p.next
                else:
                    lista.head = p.next
                if p.next is not None:
                    p.next.prev = p.prev
            else:
                p.valor = (posicao, x)
            return
        p = p.next
    if x != 0:
        lista.inserir_fim((k, x))


lista = ListaDuplamenteEncadeada()
for posicao, valor in [(4, 3), (5, 7), (10, 9), (1, 12), (9, 17)]:
    lista.inserir_fim((posicao, valor))
print(busca_por_indice(lista, 10))   # 9
print(busca_por_indice(lista, 7))    # 0 (não armazenado)
print(busca_por_valor(lista, 12))    # 1
print(busca_por_valor(lista, 99))    # -1
atualizacao(lista, 20, 5)  # posição 5 passa a valer 20
print(busca_por_indice(lista, 5))    # 20

# FUNCAO busca_por_indice: TEM COMPLEXIDADE O(m), SENDO m O NUMERO DE ELEMENTOS NAO ZERO NA LISTA
# FUNCAO busca_por_valor: TEM COMPLEXIDADE O(m), SEGUINDO A MESMA LOGICA DA FUNCAO ANTERIOR
# FUNCAO atualizacao: TEM COMPLEXIDADE O(m), POIS NO PIOR CASO TEM QUE INSERIR UM NOVO ELEMENTO NO FINAL QUE AINDA E O(m)