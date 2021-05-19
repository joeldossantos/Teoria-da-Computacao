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


#24 AFD produto
#Criar uma função que recebe dois autômatos e retorna o AFD produto entre eles.
#Atenção:
#A assinatura da função deverá ser afd_produto(automato1, automato2).
#Essa função deverá ser criada no arquivo (prop_lr.py).

#Aluno: Matheus Rodrigues Rodrigues

def afd_produto(automato1, automato2):

    estados_automato1 = list(automato1[0])
    estados_automato2 = list(automato2[0])
    dicio_automato1 = automato1(2)
    dicio_automato2 = automato2(2)
    estfinal_automato1 = list(automato1[4])
    estfinal_automato2 = list(automato2[4])

    caracteres = list(automato1(1))

    afd_prod_estados = []
    afd_prod_dicio = {}
    afd_prod_final = []

    #Cria o nome dos novos estados
    for estadocont1 in estados_automato1:

        for estadocont2 in estados_automato2:
            estado1 = estados_automato1(estadocont1)
            estado2 = estados_automato2(estadocont2)
            estado3 = estado1 + "," + estado2
            afd_prod_estados.append(estado3)

            if estado1 in estfinal_automato1 and estado2 not in estfinal_automato2:
                afd_prod_final.append(estado3)

            for caractere in caracteres:
                caractere_atual = caracteres[caractere]
                estado_relacionado1 = dicio_automato1[(estado1, caracteres[caractere])]
                estado_relacionado2 = dicio_automato2[(estado2, caracteres[caractere])]
                estado_afd_prod = estado_relacionado1 + "," + estado_relacionado2
                afd_prod_dicio[(estado3, caractere_atual)] = estado_afd_prod

    afd_produto = {set(afd_prod_estados), set(caracteres), afd_prod_dicio, string(afd_prod_estados[0]), set(afd_prod_final)}

    return afd_produto
