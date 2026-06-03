# Verificar se as listas U e V sao permutacoes uma da outra
U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
V = [7, 2, 3, 1, 6, 5, 9, 10, 4, 8]

permutacao = True

if len(U) != len(V):
    permutacao = False

for i in range(len(U)):
    cont_u = 0
    cont_v = 0

    for j in range(len(U)):
        if U[j] == U[i]:
            cont_u += 1

    for j in range(len(V)):
        if V[j] == U[i]:
            cont_v += 1

    if cont_u != cont_v:
        permutacao = False
        break

if permutacao == True:
    print("sim")
else:
    print("não")