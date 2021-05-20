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


# 34 - Descoberta de Variáveis Anuláveis
# Claudio Freitas
def anulaveis(gramatica):
    producoes = gramatica[2]
    variaveis_vazias = []
    for key in producoes:
        if len(producoes[key]) == 0:
            variaveis_vazias.append(key)
        elif type(producoes[key]) == tuple:
            for i in producoes[key]:
                if i == '':
                    variaveis_vazias.append(key)
                elif i in variaveis_vazias:
                    variaveis_vazias.append(key)
        elif len(producoes.get(key)) == 1 and i in variaveis_vazias:
            variaveis_vazias.append(key)
    return variaveis_vazias


# 35 - Eliminação de Produções Vazias
# Claudio Freitas
def remove_vazias(gramatica):
    producoes = gramatica[2]
    variaveis_vazias = anulaveis(gramatica)
    for i in variaveis_vazias:
        for key in producoes:
            if key == i:
                producoes.pop(key)
    gramatica[2] = producoes
    return gramatica


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


#Implementação número 25
#Aluno: Ricardo Buçard de Castro
def lmd(gramatica, palavra):
    palavra = str(palavra)
    palavra_aux = palavra
    producao_str = []
    inicial = gramatica[3].pop()
    saida = []
    saida.append(inicial)
    mensagem_saida = inicial
    mensagem = ''
    for producao in gramatica[2]:
        if type(producao[1]) == tuple:
            prod = str(producao[1])
            prod = prod.replace("(","")
            prod = prod.replace(")","")
            prod = prod.replace("'","")
            prod = prod.replace(",","")
            prod = prod.replace(" ","")
            producao_str.append(prod)
        else:
            prod = str(producao[1])
            producao_str.append(prod)
    while mensagem_saida != palavra:
        if len(palavra) > len(mensagem_saida) and len(palavra_aux) != 0:
            for producao in producao_str:
                if len(producao) > 2 and palavra_aux != "":
                    if palavra_aux[0] == producao[0] and palavra_aux[-1] == producao[2]:
                        mensagem_saida = mensagem_saida.replace("S", producao)
                        saida.append(mensagem_saida)
            palavra_aux = palavra_aux[1:]
            palavra_aux = palavra_aux[:-1]
        elif len(mensagem_saida) >= len(palavra):
            for producao in producao_str:
                if palavra_aux == producao:
                    mensagem_saida = mensagem_saida.replace("S", producao)
                    saida.append(mensagem_saida)
            palavra_aux = palavra_aux.replace(palavra_aux,"")
    for s in saida:
    if saida.index(s) == 0:
        producao = s[0]
        mensagem = producao
    else:
        producao = s
        mensagem += " => " + producao
    return mensagem

#Implementação número 26
#Aluno: Ricardo Buçard de Castro
def rmd(gramatica, palavra):
    palavra = str(palavra)
    palavra_aux = palavra
    producao_str = []
    inicial = gramatica[3].pop()
    saida = []
    saida.append(inicial)
    mensagem_saida = inicial
    mensagem = ''
    for producao in gramatica[2]:
        if type(producao[1]) == tuple:
            prod = str(producao[1])
            prod = prod.replace("(","")
            prod = prod.replace(")","")
            prod = prod.replace("'","")
            prod = prod.replace(",","")
            prod = prod.replace(" ","")
            producao_str.append(prod)
        else:
            prod = str(producao[1])
            producao_str.append(prod)
    while mensagem_saida != palavra:
        if len(palavra) > len(mensagem_saida) and len(palavra_aux) != 0:
            for producao in producao_str:
                if len(producao) > 2 and palavra_aux != "":
                    if palavra_aux[0] == producao[0] and palavra_aux[-1] == producao[2]:
                        mensagem_saida = mensagem_saida.replace("S", producao)
                        saida.append(mensagem_saida)
            palavra_aux = palavra_aux[:-1]
            palavra_aux = palavra_aux[1:]
        elif len(mensagem_saida) >= len(palavra):
            for producao in producao_str:
                if palavra_aux == producao:
                    mensagem_saida = mensagem_saida.replace("S", producao)
                    saida.append(mensagem_saida)
            palavra_aux = palavra_aux.replace(palavra_aux,"")
    for s in saida:
    if saida.index(s) == 0:
        producao = s[0]
        mensagem = producao
    else:
        producao = s
        mensagem += " => " + producao
    return mensagem


def vazia(gramatica): 
   simbolos_geradores = geradores(gramatica)
   simbolo_inicial = gramatica[3]
   if (simbolo_inicial not in simbolos_geradores):
      print("A GLC é vazia")
   else:
      print("A GLC não é vazia")