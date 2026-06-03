# Encontrar o elemento mais proximo da media aritmetica da lista
V = [5, 3, 1, 10, 2, 13, 9, 12, 4, 7]

soma = 0
i = 0

while i < len(V):
    soma += V[i]
    i += 1

media = soma / len(V)
i = 0
mais_prox = V[0]
menor_dis = abs(V[0] - media)
while i < len(V):
    dis_atual = abs(V[i] - media)
    if dis_atual == 0:
        print(f"a media esta na lista, o elemento {V[i]}")
        break
    elif dis_atual < menor_dis:
        menor_dis = dis_atual
        mais_prox = V[i]
    i += 1
print(f"o elemento mais proximo da media e: {mais_prox}")
