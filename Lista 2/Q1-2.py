# Encontrar o terceiro maior elemento da lista
V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

i = 0
maior = V[i]
s_maior = maior
t_maior = s_maior
while(i < len(V)):
    if V[i] > maior:
        t_maior = s_maior  # salva o antigo 2º antes de perder
        s_maior = maior    # salva o antigo 1º antes de perder
        maior = V[i]       # só agora atualiza o maior
    elif V[i] > s_maior:
        t_maior = s_maior  # salva o antigo 2º antes de perder
        s_maior = V[i]
    elif V[i] > t_maior:
        t_maior = V[i]
    i += 1
print(t_maior)