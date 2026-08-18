class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None


class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo_no = Node(valor)
        novo_no.next = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            raise IndexError("pop em pilha vazia")
        no_removido = self.topo
        self.topo = self.topo.next
        no_removido.next = None 
        return no_removido.valor

    def esta_vazia(self):
        return self.topo is None

    def imprimir(self):
        p = self.topo
        print("topo ", end="")
        while p is not None:
            print(p.valor, end=" -> ")
            p = p.next
        print("/")


class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, valor):
        novo_no = Node(valor)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.next = novo_no
            self.fim = novo_no

    def dequeue(self):
        if self.inicio is None:
            raise IndexError("dequeue em fila vazia")
        no_removido = self.inicio
        self.inicio = self.inicio.next
        if self.inicio is None:
            self.fim = None
        no_removido.next = None
        return no_removido.valor

    def esta_vazia(self):
        return self.inicio is None

    def imprimir(self):
        p = self.inicio
        print("inicio ", end="")
        while p is not None:
            print(p.valor, end=" -> ")
            p = p.next
        print("/ fim")