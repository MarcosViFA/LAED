from estruturas import FilaEncadeada

fila = FilaEncadeada()
for valor in [8, 15, 23]:
    fila.enqueue(valor)

print("Estado inicial:")
fila.imprimir()

# (a) Insere 7 e 11
fila.enqueue(7)
fila.enqueue(11)
print("\n(a) Após Enqueue(7) e Enqueue(11):")
fila.imprimir()

# (b) dois Dequeue
print("\n(b) Executando dois Dequeue:")
valor1 = fila.dequeue()
print(f"1º Dequeue removeu: {valor1}")
valor2 = fila.dequeue()
print(f"2º Dequeue removeu: {valor2}")
print("Estado após os dois Dequeue:")
fila.imprimir()