# Encontrar o maior n ́umero  ́ımpar armazenado na lista — (se houver algum)
# Find the largest odd number stored in the list — (if there is one)
V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]


biggest_odd = None
i = 0 # Place your finger on the first
while(i < len(V)):
    if V[i] % 2 != 0: # Check if it is odd.
        if biggest_odd is None or V[i] > biggest_odd:
            biggest_odd = V[i]
    i += 1
if biggest_odd is not None:
    print(biggest_odd)
else:
    print("does not exist")