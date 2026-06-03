def trocar(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def particao(lista, inicio, fim):
    pivo = lista[inicio]
    esq = inicio + 1
    dir = fim
    while esq <= dir:
        if lista[esq] <= pivo:
            esq += 1
        elif lista[dir] >= pivo:
            dir -= 1
        else:
            trocar(lista, esq, dir)
            esq += 1
            dir -= 1
    trocar(lista, inicio, dir)
    return dir


def bolha(lista, inicio, fim):
    if inicio >= fim:
        return

    temtroca = False
    for idx in range(inicio, fim):
        if lista[idx] > lista[idx + 1]:
            trocar(lista, idx, idx + 1)
            temtroca = True

    if temtroca:
        bolha(lista, inicio, fim - 1)


def particao_bolha(lista):
    if not lista:
        return lista

    k = particao(lista, 0, len(lista) - 1)

    bolha(lista, 0, k - 1)

    bolha(lista, k + 1, len(lista) - 1)

    return lista


lista = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

print(f"{lista}")
particao_bolha(lista)
print(f"{lista}")