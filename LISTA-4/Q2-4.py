from estruturas import ListaEncadeada

# Separar os elementos pares e Impares em listas diferentes

def separar_pares_impares(lista):
    lista_impares = ListaEncadeada()
    lista_pares = ListaEncadeada()
    p = lista.head
    while p is not None:
        if p.valor % 2 == 0:
            lista_pares.inserir_fim(p.valor)
        else:
            lista_impares.inserir_fim(p.valor)
        p = p.next
    return lista_impares, lista_pares


lista = ListaEncadeada()
for valor in [2, 8, 5, 10, 7]:
    lista.inserir_fim(valor)
impares, pares = separar_pares_impares(lista)
print("Ímpares: ")
impares.imprimir()
print("Pares: ")
pares.imprimir()

# O TEMPO DE EXECUCAO DESSE ALGORITIMO E DE O(n^2) POIS IRAR PERCORRER A LISTA (O(N)) E DEPOIS INSERIR NO FIM DA RESPECTIVA LISTA (IMPA OU PAR) EM O(N) TAMBEM.
# OBS: A QUESTAO NAO MENCIONA SE QUER QUE A ORDEM DAS LISTAS IMPAR E PAR SIGA A MESMA ORDEM DA LISTA ORIGINAL NESSE CASO DARIA PARA MELHORAR A EFICIENCIA DO
# ALGORITIMO TROCAND O INSERIR_FIM POR INSERIR_INICIO (O(1)) NESSE CASO O ALGORITIMO TOTAL TERIA COMPLEXIDADE O(n).