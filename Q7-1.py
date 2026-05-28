# Contar o n´umero de inversoes na lista V
V = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

total = 0
i = 0
while i < len(V):
    j = i + 1
    while j < len(V):
        if (V[i] > V[j]):
            total += 1
        j += 1
    i += 1

print(f"Total de inversoes: {total}")