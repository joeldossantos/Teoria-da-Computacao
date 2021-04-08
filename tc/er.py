#12 Transformação ER para AFN (3)
#Matheus Rodrigues Rodrigues

def er2afn_concat(expreg):
    dicio_afn = {}
    cont = 1
    for cont in len(expreg):
        atual = expreg[cont]
        if atual is tuple:
            if atual[0] == '+':
                er2afn_union(atual)
            elif atual[0] == '*' and len(atual) > 2:
                er2afn_concat(atual)
            elif atual[0] == "*" == 2:
                er2afn_kleene(atual)
        else:
            valor = ('q' + str(cont), expreg[cont])
            chave = ('q' + str(cont + 1))
            dicio_afn[valor] = chave
    i = 1
    for i in range(1, cont):
        if ('q' + str(i), 0) not in dicio_afn:
            dicio_afn[('q' + str(i), 0)] = 'q' + str(i)
        if ('q' + str(i), 1) not in dicio_afn:
            dicio_afn[('q' + str(i), 1)] = 'q' + str(i)

    return dicio_afn