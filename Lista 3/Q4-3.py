# Verificar se existem dois elementos iguais na matriz M
M = [
    [3, 9, 4, 2, 4, 1, 8, 5, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [5, 8, 2, 3, 9, 8, 4, 1, 7],
    [8, 3, 4, 2, 3, 1, 3, 9, 4],
    [3, 7, 2, 9, 4, 2, 1, 2, 3],
    [7, 5, 3, 1, 2, 4, 5, 8, 2],
    [4, 7, 3, 6, 5, 1, 9, 3, 2],
    [1, 5, 3, 2, 9, 8, 7, 6, 5],
    [3, 9, 4, 2, 4, 1, 8, 5, 1]
]


achou = False
elemento_repetido = None

i = 0
while i < len(M) and not achou:
    j = 0
    while j < len(M) and not achou:
        pivo = M[i][j]
        x = i
        while x < len(M) and not achou:
            if x == i:
                y = j + 1
            else:
                y = 0
                
            while y < len(M):
                if M[x][y] == pivo:
                    elemento_repetido = pivo
                    achou = True
                    break 
                y += 1
            x += 1
        j += 1
    i += 1

if achou:
    print(f"Sim, o elemento {elemento_repetido} aparece mais de uma vez")
else:
    print("Não existem elementos repetidos na matriz")