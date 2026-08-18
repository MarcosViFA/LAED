from estruturas import ListaDuplamenteEncadeada

# Lista de listas

def transformar_em_lista_de_listas(lista, k):
    n = 0
    p = lista.head
    while p is not None:
        n += 1
        p = p.next
    if n == 0 or k <= 0:
        return []
    tamanho_base = n // k
    resto = n % k
    L = []
    p = lista.head
    for i in range(k):
        sublista = ListaDuplamenteEncadeada()
        tamanho_desta_sublista = tamanho_base + (1 if i < resto else 0)

        for j in range(tamanho_desta_sublista):
            if p is None:
                break
            sublista.inserir_fim(p.valor)
            p = p.next

        L.append(sublista)

    return L

lista = ListaDuplamenteEncadeada()
for valor in [1, 3, 7, 10, 13, 18, 21, 27]:
    lista.inserir_fim(valor)
L = transformar_em_lista_de_listas(lista, 4)
for i, sublista in enumerate(L):
    print(f"L[{i}]: ", end="")
    sublista.imprimir()

# A COMPLEXIDADE DO ALGORITIMO SE DA EM FUNCAO DO k ESCOLHIDO NA FUNCAO transformar_em_lista_de_listas, COMO A FUNCAO IRAR DIVIDIR A LISTA EM SUBLISTAS LOGO SENDO n O
# TAMANHO DA LISTA ORIGINAL, O TAMANHO DAS SUBLISTAS DADO O k ESCOLHIDO SERA n/k, COMO TEMOS k DELAS O TOTAL FICA: n^2/k, PORTANTO A COMPLEXIDADE DO ALGORITIMO E DE O(n^2/k).