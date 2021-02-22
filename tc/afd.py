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
        estados_subpalavras.append([estado, palavra.copy()])
        return " |- ".join(["(" + str(estado_subpalavra[0]) + ", " + "".join(str(subpalavra) for subpalavra in estado_subpalavra[1]) + ")" for estado_subpalavra in estados_subpalavras])
    else:
        estados_subpalavras.append([estado, palavra.copy()])
        subpalavra = palavra.pop(0)
        estadoAtual = delta_hat(automato, estado, [subpalavra])
        return computacao(automato, estadoAtual, palavra)
