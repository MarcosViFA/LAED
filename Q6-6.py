from estruturas import PilhaEncadeada

class FilaComDuasPilhas:
    def __init__(self):
        self.p1 = PilhaEncadeada()  # entrada
        self.p2 = PilhaEncadeada()  # saída

    def enqueue(self, valor):
        self.p1.push(valor)

    def dequeue(self):
        if self.p2.esta_vazia():
            while not self.p1.esta_vazia():
                self.p2.push(self.p1.pop())

        if self.p2.esta_vazia():
            raise IndexError("dequeue em fila vazia")

        return self.p2.pop()


fila = FilaComDuasPilhas()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

print(fila.dequeue())  # 1
print(fila.dequeue())  # 2

fila.enqueue(4)
print(fila.dequeue())  # 3
print(fila.dequeue())  # 4