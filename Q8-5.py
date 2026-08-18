from estruturas import NodeDuplo, ListaDuplamenteEncadeada

# Operações na lista de listas

def encontrar_sublista(L, x):
    indice = 0
    for i in range(len(L)):
        if L[i].head is None:
            continue
        if L[i].head.valor <= x:
            indice = i
        else:
            break
    return indice


def busca(L, x):
    i = encontrar_sublista(L, x)
    p = L[i].head
    while p is not None:
        if p.valor == x:
            return True
        if p.valor > x:
            break
        p = p.next
    return False


def insercao(L, x):
    i = encontrar_sublista(L, x)
    sublista = L[i]
    novo_no = NodeDuplo(x)
    if sublista.head is None or x <= sublista.head.valor:
        novo_no.next = sublista.head
        if sublista.head is not None:
            sublista.head.prev = novo_no
        sublista.head = novo_no
        return
    p = sublista.head
    while p.next is not None and p.next.valor < x:
        p = p.next
    novo_no.next = p.next
    novo_no.prev = p
    if p.next is not None:
        p.next.prev = novo_no
    p.next = novo_no


def remocao(L, x):
    i = encontrar_sublista(L, x)
    p = L[i].head
    while p is not None:
        if p.valor == x:
            if p.prev is not None:
                p.prev.next = p.next
            else:
                L[i].head = p.next
            if p.next is not None:
                p.next.prev = p.prev
            return True
        p = p.next
    return False


L = []
for valores in [[2, 9], [15, 19], [31, 49]]:
    sublista = ListaDuplamenteEncadeada()
    for v in valores:
        sublista.inserir_fim(v)
    L.append(sublista)

print(busca(L, 19))    # True
print(busca(L, 20))    # False

insercao(L, 17)         # deve entrar na sublista [15,19] -> 15,17,19
L[1].imprimir()          # 15 <-> 17 <-> 19 <-> None

remocao(L, 9)            # remove da sublista [2,9]
L[0].imprimir()          # 2 <-> None

# FUNCAO encontrar_sublista: TEM COMPLEXIDADE O(k), SENDO k OS k-esimos PRIMEIROS EKEMENTOS DA LISTA.
# FUNCAO busca: CHAMA A FUNCAO encontrar_sublista (O(k)) E DEPOIS FAZ UM BUSCA LINEAR DENTRO DA SUBLISTA DE TAMANHO n/k LOGO A COMPLEXIDADE E DE O(k+n/k).
# FUNCAO insercao: MESMA COISA, CHAMA A FUNCAO encontrar_sublista (O(k)) DEPOIS O(n/k) PARA ACHAR A POSICAO CORRETA LOGO A COMPLEXIDADE E DE O(k+n/k).
# FUNCAO remocao: TAMBEM TEM A COMPLEXIDADE O(k+n/k) TENDO O MESMO RACIOCINIO.