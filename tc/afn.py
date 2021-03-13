'''
Autômato Finito Não Determinístico (AFN)
'''
# 2 - delta do AFN
def delta(automato, estado, simbolo):
    return automato[2][(estado, simbolo)]

# o retorno é uma lista de estados
# passando referencia da lista ao inves de valor string. A diferença no AFN ocorre  quando ele esta entrando no estado (o que ainda nao é esse parte)
