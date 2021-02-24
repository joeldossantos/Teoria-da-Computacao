'''
Autômato Finito Determinístico (AFD)
'''

estados_subpalavras = []


def delta(automato, estado, simbolo):
    return automato[2][(estado, simbolo)]


def delta_hat(automato, estado, palavra):
    if palavra == []:
        return estado
    else:
        simbolo = palavra.pop()
        return delta(automato, delta_hat(automato, estado, palavra), simbolo)


def aceita(automato, palavra):
    return delta_hat(automato, automato[3], palavra) in automato[4]


def computacao(automato, estado, palavra):
    if palavra == []:
        return "(" + estado + ", )"
    else:
        config = "(" + estado + ", " + printw(palavra) + ") |- "
        simbolo = palavra.pop(0)
        proximo = delta(automato, estado, simbolo)
        return config + computacao(automato, proximo, palavra)


def printw(palavra):
    return "".join(str(simbolo) for simbolo in palavra)