import tc.afd

# Recebe um AFD
# Olhe o arquivo unit.py para ter exemplos de entrada e saída da função
def tfa_table(automato): 
    estados = list(automato[0])
    estados.sort()
        
    table = []

    for i, estado1 in enumerate(estados[:-1]):
        for estado2 in estados[i+1:]:
            table.append([estado1, estado2, ''])
    
    return table

def tfa_fill(automato):
    table = prop_lr.tfa_table(automato)
    table_aux = []

    for pair in table:
        # Se apenas um dos dois estados do par for final, o par é distinguivel
        if (pair[0] in automato[4]) != (pair[1] in automato[4]):
            pair[2] = 'd'
        else:
            table_aux.append(pair)
    
    achou_novos = True

    while achou_novos:
        # Caso não encontre nenhum par novo que seja distinguivel, o algoritmo chegou ao fim
        achou_novos = False
        for pair in table_aux:
            for simbolo in automato[1]:
                r = s = []
                try:
                    r = afd.delta(automato, pair[0], simbolo)
                    s = afd.delta(automato, pair[1], simbolo)
                except KeyError:
                    continue

                try:
                    table.index([r, s, 'd'])
                except ValueError:
                    pass
                else:
                    pair[2] = 'd'
                    try:
                        table_aux.remove(pair)
                    except:
                        pass
                    achou_novos = True
                
                try:
                    table.index([s, r, 'd'])
                except ValueError:
                    pass
                else:
                    pair[2] = 'd'
                    try:
                        table_aux.remove(pair)
                    except:
                        pass
                    achou_novos = True

    # Para cada par que não for distinguivel, marcá-lo como indistinguivel
    for pair in table:
        if pair[2] != 'd':
            pair[2] = 'i'

    return table

def tfa(automato):
    
    t = tfa_table(automato)
    table = tfa_fill(automato,t)
    y = []
    
    for x in table:
        if(x[2] == ''):
            y.append([x[0],x[1]])

    eq = set(tuple(i) for i in y)
    return eq


