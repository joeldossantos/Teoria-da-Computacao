'''
Autômato Finito Determinístico (AFD)
'''


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
    subpalavras = [[]]
    aux = []
    output = []

    for i in palavra:
        aux.append(i)
        subpalavras.append(aux.copy())

    subpalavras.reverse()

    for i in subpalavras:
        output.append([i.copy(), delta_hat(automato, estado, i)])

    return " |- ".join(["(" + x[1] + ", " + "".join(str(x) for x in x[0]) + ")" for x in output])
