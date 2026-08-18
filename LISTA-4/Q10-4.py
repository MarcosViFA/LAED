from estruturas import ListaEncadeada

# Construir uma terceira lista que cont´em todos os elementos que aparecem
# em ambas as listas

def intersecao(lista1, lista2):
    resultado = ListaEncadeada()
    p1 = lista1.head
    while p1 is not None:
        p2 = lista2.head
        encontrou = False
        while p2 is not None:
            if p2.valor == p1.valor:
                encontrou = True
                break
            p2 = p2.next
        if encontrou:
            resultado.inserir_fim(p1.valor)
        p1 = p1.next
    return resultado


lista1 = ListaEncadeada()
for valor in [3, 9, 2, 6, 4]:
    lista1.inserir_fim(valor)
lista2 = ListaEncadeada()
for valor in [4, 5, 2, 9, 3]:
    lista2.inserir_fim(valor)
p = intersecao(lista1, lista2)
p.imprimir()

# COMO TEMOS QUE PERCORRER AS 2 LISTAS E TEMOS 2 LACOS CONCATENADOS, O TEMPO DE EXECUCAO DO ALGORITIMO E DE O(n*m) SENDO N E M OS RESPECTIVOS TAMANHOS DOS VETORES.