# (a) Estrutura de dados:
class NoComMinimo:
    def __init__(self, valor, minimo_ate_aqui):
        self.valor = valor
        self.minimo_ate_aqui = minimo_ate_aqui  # menor valor da pilha, considerando este nó e os de baixo
        self.next = None

# (b) Implementacao de Push, Pop e Min, todos O(1):

class PilhaComMinimo:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        if self.topo is None:
            minimo = valor
        else:
            minimo = min(valor, self.topo.minimo_ate_aqui)

        novo_no = NoComMinimo(valor, minimo)
        novo_no.next = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            raise IndexError("pop em pilha vazia")
        no_removido = self.topo
        self.topo = self.topo.next
        no_removido.next = None
        return no_removido.valor

    def min(self):
        if self.topo is None:
            raise IndexError("pilha vazia, não há mínimo")
        return self.topo.minimo_ate_aqui

    def imprimir(self):
        p = self.topo
        print("topo ", end="")
        while p is not None:
            print(f"{p.valor}(min={p.minimo_ate_aqui})", end=" -> ")
            p = p.next
        print("/")

# (c) Trace da execucao:

pilha = PilhaComMinimo()
pilha.push(5)
pilha.imprimir()
pilha.push(3)
pilha.imprimir()
pilha.push(7)
pilha.imprimir()
pilha.push(1)
pilha.imprimir()
valor_removido = pilha.pop()
print(f"Pop removeu: {valor_removido}")  # Pop removeu: 1
pilha.imprimir()
print(f"Min: {pilha.min()}")  # Min: 3