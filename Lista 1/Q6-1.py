# Encontrar os dois elementos da lista L que possuem a menor
# diferenca entre si — (em valor absoluto)
V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

num_1 = V[0]
num_2 = V[1]
menor_dif = abs(num_1 - num_2)
i = 0
for i in range(len(V)):
    j = i + 1
    for j in range(i+1, len(V)):
        dif = abs(V[i] - V[j])
        if dif < menor_dif:
            menor_dif = dif
            num_1 = V[i]
            num_2 = V[j]
print(f"Os elementos {num_1} e {num_2}")