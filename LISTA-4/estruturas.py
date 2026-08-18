class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_fim(self, valor):
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = novo_no

    def inserir_inicio(self, valor):
        novo_no = Node(valor)
        novo_no.next = self.head
        self.head = novo_no

    def imprimir(self):
        p = self.head
        while p is not None:
            print(p.valor, end=" -> ")
            p = p.next
        print("None")