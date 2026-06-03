# Verificar a matriz M contém duas linhas exatamente iguais
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

for i in range(len(M)):
    for j in range(i + 1, len(M)):
        if M[i] == M[j]: # O Python compara todos os elementos internamente
            print(f"Sim, as linhas {i+1} e {j+1} são exatamente iguais")
            achou = True
            break
    if achou:
        break