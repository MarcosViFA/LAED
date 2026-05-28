# Procurar o numero k na lista L, e se ele nao estiver la
# retornar o elemento da lista com o valor mais proximo de k
V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

k = 1
mais_proximo = None
menor_dis = None
i = 0
while i < len(V):
    dis_atual = abs(V[i] - k)
    if dis_atual == 0:
        print("numero na lista")
        break
    elif menor_dis is None or dis_atual < menor_dis:
        menor_dis = dis_atual
        mais_proximo = V[i]
    i += 1
print(mais_proximo)