# Verificar se existe algum numero ımpar
# que aparece um numero ımpar de vezes na lista
V = [9, 2, 7, 7, 7, 2, 2, 1, 7, 7, 9]

i = 0
for i in range(len(V)):
    if V[i] % 2 != 0:
        cont = 0
        j = 0
        for j in range(len(V)):
            if V[i] == V[j]:
                cont += 1
        if cont % 2 != 0:
            print(f"Sim o {V[i]}")
            break
