from estruturas import ListaEncadeada

# Determinar se a lista contem algum elemento repetido ou nao

def tem_repetido(lista):
    vistos = set()
    p = lista.head
    while p is not None:
        if p.valor in vistos:
            return True
        vistos.add(p.valor)
        p = p.next
    return False


lista = ListaEncadeada()
for valor in [2, 9, 7, 4, 9, 1]:
    lista.inserir_fim(valor)
if tem_repetido(lista):
    print("Sim")
else:
    print("Não")

# O USO DO set AJUDA NA COMPLEXIDADE POIS A LINHA 9 EXECUTA EM TEMPO O(1), PORTANTO A COMPLEXIDADE DO ALGORITIMO E O(n) POIS VAI PERCORRER O VETOR POR COMPLETO.