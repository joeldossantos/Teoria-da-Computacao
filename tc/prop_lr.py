
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
