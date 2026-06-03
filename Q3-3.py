def mediana_listas_ordenadas(U, V):

    n = len(U)
    ini_u, fim_u = 0, n - 1
    ini_v, fim_v = 0, n - 1

    while True:
        tamanho = fim_u - ini_u + 1
        if tamanho == 1:
            return min(U[ini_u], V[ini_v])
        
        if tamanho == 2:
            return max(U[ini_u], V[ini_v])
        
        meio_u = ini_u + (tamanho - 1) // 2
        meio_v = ini_v + (tamanho - 1) // 2

        m1 = U[meio_u]
        m2 = V[meio_v]

        if m1 == m2:
            return m1

        elif m1 < m2:
            if tamanho % 2 == 0:
                ini_u = meio_u + 1
                fim_v = meio_v
            else:
                ini_u = meio_u
                fim_v = meio_v

        else:
            if tamanho % 2 == 0:
                fim_u = meio_u
                ini_v = meio_v + 1
            else:
                fim_u = meio_u
                ini_v = meio_v


U = [1, 6, 10, 15, 19]
V = [3, 7, 11, 17, 21]
mediana = mediana_listas_ordenadas(U, V)
print(f"A mediana global encontrada é: {mediana}")