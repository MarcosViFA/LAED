from estruturas import FilaEncadeada

def radix_sort(numeros, num_digitos):
    numeros = list(numeros)

    for casa in range(num_digitos):
        filas = [FilaEncadeada() for _ in range(10)]
        for numero in numeros:
            digito = (numero // (10 ** casa)) % 10
            filas[digito].enqueue(numero)
        numeros = []
        for fila in filas:
            while not fila.esta_vazia():
                numeros.append(fila.dequeue())

    return numeros


sequencia = [481, 329, 143, 612, 937, 480, 256]
resultado = radix_sort(sequencia, num_digitos=3)
print(resultado)