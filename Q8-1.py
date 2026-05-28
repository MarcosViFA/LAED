# Imprimir todos os numeros que aparecem nas duas listas
U = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
V = [2, 15, 19, 12, 33, 9, 17, 41, 54, 8]

i = 0
AUX = []
for i in range(len(U)):
    j = 0
    for j in range(len(V)):
        if U[i] == V[j]:
            if U[i] not in AUX:
                AUX.append(U[i])

for elm in AUX:
    print(elm)