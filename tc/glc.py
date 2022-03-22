import itertools


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
# Algoritmo reescrito por Gabriel Lima de Souza em 2022, pois não atendia nenhum requisito.
# Código antigo por Dennis Rodrigues
# Código antigo por Gabriel Souto
# 28 Gramática Regular
def regular(gramatica):
    # print("USANDO ORIGINAL")
    variaveis = gramatica[0]
    terminais = gramatica[1]
    producoes = gramatica[2]
    gld = False
    gle = False

    for producao in producoes:
        lado_direito = None
        if isinstance(producao[1], tuple) or  isinstance(producao[1], list) or isinstance(producao[1], str):
            lado_direito = producao[1]
        else:
            lado_direito = [producao[1]]

        
        for variavel in variaveis:
            # print(variavel, " aparece ", producao[1].count(variavel), " vezes")
            aparicoes = lado_direito.count(variavel)
            if aparicoes > 1:
                return "Gramatica não Regular"
            elif aparicoes == 1:
                if lado_direito[len(lado_direito) - 1] == variavel:
                    if gle == True:
                        return "Gramatica não Regular"
                    else:
                        gld = True
                    # print("Vai ser direita")
                elif lado_direito[0] == variavel:
                    if gld == True:
                        return "Gramatica não Regular"
                    else:
                       gle = True
                    # print("Vai ser esquerda")
                else:
                    return "Gramatica não Regular"
                
        # print("\n")

    if gld == True and gle == False:
        return "Gramática Linear à Direita"
    elif gle == True and gld == False:
        return "Gramática Linear à Esquerda"
    else:
        return "Gramatica não Regular"


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

#Algoritmo reescrito por Gabriel Lima de Souza em 2022
def vazia(gramatica): 
    variaveis = gramatica[0]
    terminais = gramatica[1]
    producoes = gramatica[2]
    inicial = gramatica[3]

    var_marcadas = terminais

    # print("Variaveis: ", variaveis)
    # print("Terminais: ", terminais)
    # print("Producoes: ", producoes)

    # print("Inicial: ", inicial)

    # # var_marcadas.add('S')

    # print("Variaveis Marcadas: ", var_marcadas)

    # print("\n\n\n")

    continua_checagem = True

    while continua_checagem:
        continua_checagem = False
        for var_atual in variaveis:
            marca_var_atual = True
            # print("Variável atual: ",  var_atual)

            if var_atual in var_marcadas:
                # var_marcadas.append(var_atual)
                # print("Pulando variavel ", var_atual, " ja marcada")
                continue

            for producao in producoes:

                #Variáveis para facilitar leitura da produção
                ld_esq = producao[0]
                ld_dir= None
                if isinstance(producao[1], tuple) or  isinstance(producao[1], list) or isinstance(producao[1], str):
                    ld_dir = producao[1]
                else:
                    ld_dir = [producao[1]]
                
                

                if ld_esq == var_atual:

                    # print("Produção atual: ", producao)
                    # print("Lado direito marcado: ", set(ld_dir).issubset(var_marcadas))

                    if set(ld_dir).issubset(var_marcadas) == False:
                        # print("NÃO VAI MARCAR")
                        marca_var_atual = False
                        break

                    # print("\n")

            if marca_var_atual:
                var_marcadas.add(var_atual)
                continua_checagem = True
            # print("\n\n")


            # print("Variaveis Marcadas:", var_marcadas)

    # print("É vazia? ", (inicial in var_marcadas))

    if inicial in var_marcadas:
        return "A GLC não é vazia"
    
    return "A GLC é vazia"


#    simbolos_geradores = geradores(gramatica)
#    simbolo_inicial = gramatica[3]
#    if (simbolo_inicial not in simbolos_geradores):
#       print("A GLC é vazia")
#    else:
#       print("A GLC não é vazia")



#36 Descoberta de Pares Unitários
#Marcos Eduardo Carvalho Teixeira
def unitarios(gramatica):
    variaveis, terminais, producoes, simboloInicial = gramatica

    pares = list([])
    paresBase  = []

    variaveisLista = list(variaveis)
    producoesList = list(producoes)

    for vari in variaveisLista:
        paresBase.append((vari,vari))

    for prod in producoesList:
        if len(prod[1])==1 and prod[1] in variaveisLista:
            pares.append((prod[0], prod[1])) 

    permutacoes = list(itertools.permutations(pares))

    paresSeq = []
    for p in permutacoes:
        aux = p[0]
        seq = [aux]
        for t in p:
            if aux[1] == t[0]:
                seq.append(t)
                aux = t
        cabeca = seq[0]
        cauda = seq[-1]
        tupla = (cabeca[0],cauda[1])
        paresSeq.append(tupla)

    return set(paresSeq + paresBase + pares)


#37 Eliminação de Produções Unitárias
#Marcos Eduardo Carvalho Teixeira
def remove_unitarias(gramatica):

    variaveis, terminais, producoes, simboloInicial = gramatica

    variaveisLista = list(variaveis)
    producoesList = list(producoes)

    paresUnitarios = unitarios(G)


    prodUniDiretas = producoesList.copy()
    for prod in prodUniDiretas:
        if len(prod[1])==1 and prod[1] in variaveisLista:
            prodUniDiretas.remove(prod)


    producoesNovas = []
    for par in paresUnitarios:
        for prod in prodUniDiretas:
            if par[1]==prod[0]:
                producoesNovas.append((par[0], prod[1]))

    return (variaveis,terminais,set(producoesNovas),'S')
