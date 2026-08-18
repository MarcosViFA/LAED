from estruturas import ListaEncadeada

# Encontrar o elemento que aparece mais vezes na lista

def elemento_mais_frequente(lista):
    contagem = {}
    p = lista.head
    while p is not None:
        if p.valor in contagem:
            contagem[p.valor] += 1
        else:
            contagem[p.valor] = 1
        p = p.next
    mais_frequente = None
    maior_contagem = 0
    for valor, qtd in contagem.items():
        if qtd > maior_contagem:
            maior_contagem = qtd
            mais_frequente = valor
    return mais_frequente, maior_contagem


lista = ListaEncadeada()
for valor in [8, 3, 8, 5, 8, 3, 3, 3]:
    lista.inserir_fim(valor)
valor, qtd = elemento_mais_frequente(lista)
print(f"{valor} é o elemento que aparece mais vezes, com {qtd} ocorrências")

# O USO DO DICIONARIO ECONOMIZOU COMPLEXIDADE, LOGO O TEMPO DE EXECUCAO DO ALGORITIMO SERA O(n) POIS APENAS PERCORREMOS VETOR E FOMOS GUARDANDO AS INFORMACOES NO DICIONARIO