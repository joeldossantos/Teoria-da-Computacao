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