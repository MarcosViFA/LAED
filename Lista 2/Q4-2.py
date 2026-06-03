# Verificar se a lista contem algum elemento isolado
v = [17, 2, 8, 1, 7, 13, 9, 12, 4, 16]

nenhum = True
for i in range(len(v)):
    isolado = True
    for j in range(len(v)):
        k1 = v[i]+1
        k2 = v[i]-1
        if v[j] == k1 or v[j] == k2:
            isolado = False
    if isolado:
        nenhum = False
        print(f"o numero {v[i]} é isolado")

if nenhum:
    print("não tem nenhum numero isolado")