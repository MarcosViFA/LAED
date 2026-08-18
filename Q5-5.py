from estruturas import ListaDuplamenteEncadeada

# Vetores esparsos

def construir_vetor_esparso(vetor):
    lista = ListaDuplamenteEncadeada()
    for posicao, valor in enumerate(vetor, start=1):
        if valor != 0:
            lista.inserir_fim((posicao, valor))  # guarda a tupla (posição, valor)
    return lista


def imprimir_esparso(lista):
    p = lista.head
    while p is not None:
        posicao, valor = p.valor
        print(f"({posicao}, {valor})", end=" <-> ")
        p = p.next
    print("None")


v = [0, 3, 0, 0, 0, 5, 0, 2, 0, 0, 8, 0, 0, 7, 0]
lista = construir_vetor_esparso(v)
imprimir_esparso(lista)
# OBSERVACAO: O PRIMEIRO ELEMENTO DO PAR ORDENADO(TUPLA) RETORNADO SIGNIFICA A POSICAO E O SEGUNDO O VALOR
# A COMPLEXIDADE DO ALGORITIMO NO PIOR CASO COM A SOMA DAS INSERCOES PODE CHEGAR A O(m^2), ONDE M E O NUMERO DE ELEMENTOS NAO ZERO, EM GERAL O TEMPO DE EXECUCAO DO ALGORITIMO
# E DE O(n + (m^2)).