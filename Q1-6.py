from estruturas import PilhaEncadeada

pilha = PilhaEncadeada()
for valor in [5, 17, 42]:
    pilha.push(valor)

print("Estado inicial:")
pilha.imprimir()

# (a) Push(topo, 99) e depois Push(topo, 3)
pilha.push(99)
pilha.push(3)
print("\n(a) Apos Push(99) e Push(3):")
pilha.imprimir()

# (b) dois Pop
print("\n(b) Executando dois Pop:")
valor1 = pilha.pop()
print(f"1º Pop removeu: {valor1}")
valor2 = pilha.pop()
print(f"2º Pop removeu: {valor2}")
print("Estado apos os dois Pop:")
pilha.imprimir()

#