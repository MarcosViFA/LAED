# Verificar se existem dois elementos na lista L tais que
# um deles e o dobro do outro
V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
V.sort()

#CASO DESORDENADO
'''
i = 0
while i < len(V):
    j = 0
    while j < len(V):
        if V[i] == 2 * V[j]:
            print(f"Sim, o {V[i]} e {V[j]}")
        j += 1
    i += 1
'''
#CASO ORDENADO
i = 0
j = 1
while i < len(V) and j < len(V):
    if V[j] == 2 * V[i]:
        print(f"Sim, o {V[i]} e {V[j]}")
        j += 1
    elif V[j] < 2 * V[i]:
        j += 1
    else:
        i += 1
    if i == j:
        j += 1