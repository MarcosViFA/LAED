class NodeDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None

    def inserir_fim(self, valor):
        novo_no = NodeDuplo(valor)
        if self.head is None:
            self.head = novo_no
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = novo_no
        novo_no.prev = p

    def imprimir(self):
        p = self.head
        while p is not None:
            print(p.valor, end=" <-> ")
            p = p.next
        print("None")