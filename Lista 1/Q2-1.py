# Encontrar o segundo maior numero ımpar armazenado na lista — (se ele existir)
# Find the second largest odd number stored in the list — (if there is one)
V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

largest_odd = None
second_largest_odd = None
i = 0
for i in range(len(V)):
    if (V[i] % 2 != 0):
        if largest_odd is None or V[i] > largest_odd:
            second_largest_odd = largest_odd
            largest_odd = V[i]
        elif second_largest_odd is None or V[i] > second_largest_odd:
            second_largest_odd = V[i]

if second_largest_odd is not None:
    print(second_largest_odd)
else:
    print("does not exist")