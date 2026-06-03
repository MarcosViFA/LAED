# Verificar se existe algum elemento que aparece ao menos k vezes na lista
V = [7, 1, 9, 1, 7, 3, 9, 2, 1, 6, 8, 3, 3]

k = 3
i = 0

while i < len(V):
    repetido = False
    j = 0
    while j < i:
        if V[i] == V[j]:
            repetido = True
            break
        j += 1
    if not repetido:
        cont = 0
        j = 0
        while j < len(V):
            if V[j] == V[i]:
                cont += 1
            j += 1

        if cont == k:
            print(f"Sim, o elemento {V[i]}")
    i += 1