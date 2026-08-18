from estruturas import PilhaEncadeada, FilaEncadeada

def inverter_fila(fila):
    pilha_auxiliar = PilhaEncadeada()
    while not fila.esta_vazia():
        valor = fila.dequeue()
        pilha_auxiliar.push(valor)

    while not pilha_auxiliar.esta_vazia():
        valor = pilha_auxiliar.pop()
        fila.enqueue(valor)


fila = FilaEncadeada()
for valor in [1, 2, 3, 4]:
    fila.enqueue(valor)
print("Antes:")
fila.imprimir()
inverter_fila(fila)
print("Depois:")
fila.imprimir()