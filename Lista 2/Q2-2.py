# Encontrar o k-esimo maior elemento da lista
V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
k = 4
A = [0] * k

i = 0
j = 0
while j < len(V):
    x = V[j]
    w = 0
    achou = False
    while w <= k - 1 and achou == False:
        if x > A[w]:
            m = k - 1
            while m > w:
                A[m] = A[m-1]
                m -= 1
            A[w] = x
            achou = True
        w += 1
    j += 1

print(A[k-1])

# Tempo de execucao O(len(V) * k)