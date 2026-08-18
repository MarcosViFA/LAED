from estruturas import PilhaEncadeada

ABRIDORES = {'(', '[', '{'}
FECHADORES = {')', ']', '}'}
PAR_CORRESPONDENTE = {')': '(', ']': '[', '}': '{'}

def verificar_balanceamento(expressao):
    pilha = PilhaEncadeada()

    for posicao, caractere in enumerate(expressao):
        if caractere in ABRIDORES:
            pilha.push(caractere)
        elif caractere in FECHADORES:
            if pilha.esta_vazia():
                return False, posicao, caractere, "fechador sem abridor correspondente"

            topo = pilha.pop()
            esperado = PAR_CORRESPONDENTE[caractere]
            if topo != esperado:
                return False, posicao, caractere, f"esperava fechar '{topo}', encontrou '{caractere}'"

    if not pilha.esta_vazia():
        return False, len(expressao), None, "abridor sem fechador correspondente (sobrou na pilha)"

    return True, None, None, None


def testar(expressao):
    valida, posicao, caractere, motivo = verificar_balanceamento(expressao)
    if valida:
        print(f"'{expressao}' -> válida")
    else:
        print(f"'{expressao}' -> INVÁLIDA (posição {posicao}, '{caractere}': {motivo})")


testar("({[]})")
testar("({[)}]")
testar("({[]}[()]{})")