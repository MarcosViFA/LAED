# Verificar se existem dois elementos repetidos
# que se encontram a distancia no maximo k um do outro
V = [2, 1, 9, 7, 6, 3, 9, 4, 2, 6, 1, 3]

i = 0
k = 4
encontrou = False

while i < len(V):
    j = i + 1
    while j <= i+k and j < len(V):
        if V[j] == V[i]:
            print(f"Sim o {V[i]}")
            encontrou = True
            break
        j += 1
    if encontrou:
        break
    i += 1