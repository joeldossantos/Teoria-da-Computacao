
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


def tfa(automato):
    
    t = tfa_table(automato)
    table = tfa_fill(automato,t)
    y = []
    
    for x in table:
        if(x[2] == ''):
            y.append([x[0],x[1]])

    eq = set(tuple(i) for i in y)
    return eq


