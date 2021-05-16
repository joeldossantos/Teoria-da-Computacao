### Transformação de AF para GR

def afd2gr(automato):
    V = set()
    T = set()
    P = set()
    S = automato[3]
    G = (V, T, P, S)
    indice = 0
    listaDelta = list(automato[2].values())
    for terminal in automato[1]:
        aux = set(terminal)
        T.update(aux)
    for estado in automato[0]:
        conjunto_estado = [estado]
        aux = set(conjunto_estado)
        V.add(estado)
    for chave in automato[2]:
        conjunto_producoes = [(chave[0],(chave[1],listaDelta[indice]))]
        aux = set(conjunto_producoes)
        P.update(aux)
        indice+=1
    for final in automato[4]:
        conjunto_terminais = [(final,'')]
        aux = set(conjunto_terminais) 
        P.update(conjunto_terminais)


# 28 - Gramática Regular
# Dennis Rodrigues
def regular(gramatica):
    producoes = gramatica[2]
    terminais = gramatica[1]
    variaveis = gramatica[0]

    regular_direita = False
    regular_esquerda = False

    for producao in producoes:
        variavel = 0
        temp1 = ''
        temp2 = ''

        if(type(producao[1]) == tuple) and (len(producao[1]) > 0):
            for i in producao[1]:
                if i in terminais:
                    temp1 += str(i)
                elif i in variaveis:
                    variavel += 1
                    temp1 += str(i)
                    temp2 = str(i)
                    if variavel > 1:
                        return 'A gramatica contem mais do que uma variavel como derivacao de uma das producoes, logo nao e regular.'
            if temp2 in temp1[0]:
                regular_esquerda = True    
                continue
            elif temp2 in temp1[-1]:
                regular_direita = True
                continue
            else:
                return 'A gramatica nao e regular. Contem uma variavel que nao fica a direita e nem a esquerda.'
            
    if regular_esquerda and not regular_direita:
        return 'A gramatica e regular a esquerda.'
    elif regular_direita and not regular_esquerda:
        return 'A gramatica e regular a direita.'
    else:
        return 'A gramatica nao e regular.'

def fng_e1(gramatica):
    # TODO
    return gramatica

def fng_e2(gramatica):
    # TODO
    return gramatica

def fng_e3(gramatica):
    # TODO
    return gramatica

def fng_e4(gramatica):
    # TODO
    return gramatica

def fng(gramatica):
    # 1 - Renomeia as variáveis em forma crescente
    etapa1 = fng_e1(gramatica)

    # 2 - Garantir que r é menor ou igual a s, ou seja, ( A_r -> [A_s, α] ) | r <= s
    etapa2 = fng_e2(etapa1)

    # 3 - Remover recursão a esquerda das produções ( A_r -> [A_s, α] )
    etapa3 = fng_e3(etapa2)

    # 4 - Colocar as produções com terminal no início do lado direito
    etapa4 = fng_e4(etapa3)

    return etapa4
