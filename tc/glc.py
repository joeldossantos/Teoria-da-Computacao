# Transformação de AF para GR

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
        conjunto_producoes = [(chave[0], (chave[1], listaDelta[indice]))]
        aux = set(conjunto_producoes)
        P.update(aux)
        indice += 1
    for final in automato[4]:
        conjunto_terminais = [(final, '')]
        aux = set(conjunto_terminais)
        P.update(conjunto_terminais)
        
## 31 - Descoberta de Simbolos Geradores (Ramon Grande Da Luz Bouças)
def simbolo_gerador(gramatica,simbolo,fila):
    print (fila)
    V,T,P,S = gramatica
    
    ## se o símbolo analisado for um terminal, ele é gerador
    if simbolo in T:
        return True
    
    ## temos uma fila de simbolos aguardando decisao, e se formos analisar um simbolo que está aguardando decisão 
    ## caimos em uma recursao sem limite, por isso, nesses casos precisamos considerar o simbolo como falso temporariamente
    ## para poder analisar outras produçoes
    if simbolo in fila:
        return False
    
    ## se o simbolo já foi adicionado antes no conjunto dos geradores, ele é gerador
    ## (idéia de programação dinâmica pra não analisar varias vezes o mesmo simbolo)
    #if simbolo in conjunto_geradores: 
     #   return True
    
    ## pega todas as produçoes em que o simbolo analisado é a cabeça
    lista_producoes = [prod for prod in P if prod[0] == simbolo]
    
    ## analisa todas as produçoes para ver se há PELO MENOS UMA produção que atende as condições necessárias
    for producao in lista_producoes:
        corpo = producao[1]
        ## analisa os simbolos da produção para ver se TODOS os símbolos são geradores
        for simb in corpo:
            ## chama a função de forma recursiva para saber se o simbolo é gerador
            resp = simbolo_gerador(gramatica,simb,fila | {simbolo})
            if(resp == False):
                ## se algum simbolo do corpo da produção não é gerador
                ## a produção não serve para mostrar que a cabeça é geradora
                ## então passamos a analisar a proxima produção
                continue
        ## se chegamos aqui, achamos uma produção em que todos os simbolos sao geradores,
        ## então retornamos True, para indicar que a palavra é geradora
        return True
    
    return False   

def geradores(gramatica):
    ## decompoe a gramatica em variáveis, terminais, produçoes e simbolo inicial
    V,T,P,S = gramatica

    ## inicializa um conjunto vazio que será preenchido com os símbolos geradores
    simbolos_geradores = set({})
    
    
    for variavel in V:
        ## verifica se a variavel é geradora
        resp = simbolo_gerador(gramatica,variavel,fila = set({}))
        
        ## caso a variavel seja geradora, adiciona ela ao conjunto de simbolos geradores
        if(resp == True):
            simbolos_geradores = simbolos_geradores | {variavel}
        
    ## adiciona todas os terminais no conjunto de simbolos geradores    
    simbolos_geradores = simbolos_geradores | T
    
    return simbolos_geradores

# 28 - Gramática Regular
# Dennis Rodrigues
# Gabriel Souto
# 28 Gramática Regular
def regular(gramatica):
    variaveis = gramatica[0]
    terminais = gramatica[1]
    producoes = gramatica[2]
    gld = False
    gle = False
    variavel = variaveis.pop()
    variaveis.add(variavel)
    mensagem = ''

    if len(variaveis) > 1:
        mensagem = "Gramatica não Regular"
    else:
        # Gramatica regular
        for producao in producoes:
            if not (isinstance(producao[1], int) or isinstance(producao[1], str)) and producao[1]: 
                corpo_producao = producao[1]
                print(corpo_producao)
                if corpo_producao.count(variavel) == 1:
                    if corpo_producao[0] in variaveis: 
                        gle = True
                    else:
                        gle = False
                        break
                else:
                    gle = False
                    break

        for producao in producoes:
            if not (isinstance(producao[1], int) or isinstance(producao[1], str)) and producao[1]: 
                corpo_producao = producao[1]
                if corpo_producao.count(variavel) == 1:
                    if corpo_producao[-1] in variaveis:
                        gld = True
                    else:
                        gld = False
                        break
                else:
                    gld = False
                    break

        if gle:
            mensagem = 'Gramática Linear à Esquerda'
        elif gld:
            mensagem = 'Gramática Linear à Direita'
        elif not gld and not gle:
            mensagem = 'Gramatica não Regular'

    return mensagem

## 29 - Transformação de GR para AF (Autômato com Pilha)
# Rodrigo Meira Lima de Campos
def gr2afn(gramatica):
    variaveis = gramatica[0]
    terminais = gramatica[1]
    producoes = gramatica[2]
    f_transicao = {}
    i = 0

    for v in variaveis:
        f_transicao[('q', ' ', v)] = set()
        for p in producoes:
            if(p[0] == v):
               # print('Funcao de transicao para', v)
                derivacoes = p[1]
                for d in derivacoes:
                    conjunto = f_transicao[('q', ' ', v)]
                    conjunto.add(('q', d))
                    f_transicao[('q', ' ', v)] = conjunto
                    i += 1

    for t in terminais:
        f_transicao[('q', t, t)] = ('q', ' ')
        #conjunto = f_transicao[('q', t, t)]
       # conjunto.add()

    pilha = ({'q'}, terminais, variaveis.union(
        terminais), f_transicao, gramatica[3])
    return pilha

# 42 Forma Normal de Greibach - Passo 2 - Rodrigo Meira Lima de Campos


def fng_e2(gramatica):
    variaveis = gramatica[0]
    terminais = gramatica[1]
    producoes = gramatica[2]
    inicio = gramatica[3]

    for t in producoes:
        var1 = t[0]
        var2 = t[1]
        for s in var2:
            r = int(var1[1])
            sub = ''
            for j in s:
                sub = sub + j
                if str.isdigit(j):
                    s = int(j)
                    if r > s:
                        for j2 in var2:
                            if str(s) in j2:
                                tupla_direita = t[1]
                                for i in range(0, len(tupla_direita)):
                                    temp = tupla_direita[i]

                    else:
                        break

    gramatica = (variaveis, terminais, producoes, 'A1')
    return gramatica

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


# Implementação número 25
# Aluno: Ricardo Buçard de Castro
def lmd(gramatica, palavra):
    palavra = str(palavra)
    palavra_aux = palavra
    producao_str = []
    inicial = gramatica[3]
    saida = []
    saida.append(inicial)
    mensagem_saida = inicial
    mensagem = ''
    for producao in gramatica[2]:
        if type(producao[1]) == tuple:
            prod = str(producao[1])
            prod = prod.replace("(", "")
            prod = prod.replace(")", "")
            prod = prod.replace("'", "")
            prod = prod.replace(",", "")
            prod = prod.replace(" ", "")
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
            palavra_aux = palavra_aux.replace(palavra_aux, "")
    for s in saida:
        if saida.index(s) == 0:
            producao = s[0]
            mensagem = producao
        else:
            producao = s
            mensagem += " => " + producao
    return mensagem

# Implementação número 26
# Aluno: Ricardo Buçard de Castro


def rmd(gramatica, palavra):
    palavra = str(palavra)
    palavra_aux = palavra
    producao_str = []
    inicial = gramatica[3]
    saida = []
    saida.append(inicial)
    mensagem_saida = inicial
    mensagem = ''
    for producao in gramatica[2]:
        if type(producao[1]) == tuple:
            prod = str(producao[1])
            prod = prod.replace("(", "")
            prod = prod.replace(")", "")
            prod = prod.replace("'", "")
            prod = prod.replace(",", "")
            prod = prod.replace(" ", "")
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
            palavra_aux = palavra_aux.replace(palavra_aux, "")
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
