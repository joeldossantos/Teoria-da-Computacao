#10 Transformação ER para AFN (1)
#Lucas de Andrade Fernandes Leite

def er2afn_base(expreg):

    if type(expreg) is tuple:
        expreg = expreg[0]
    QSet = {} 
    Sigma = {}
    Delta = {}
    FSet = {}
    if expreg in {'0', '1'}:
        QSet = {'q1', 'q2'}
        FSet = {'q2'}
        Sigma = {'0', '1'}
        Delta = {
            ('q1', expreg): 'q2'
        }
    elif expreg = '':
        QSet = {'q1'}
        FSet = {'q1'}
        Sigma = {'0', '1'}
        Delta = {}
    elif not expreg:
        QSet = {'q1'}
        FSet = {}
        Sigma = {'0', '1'}
        Delta = {}

    automato = (QSet, Sigma, Delta, 'q1', FSet)

    return automato

#11 Transformação ER para AFN (2)
# Matheus Santos Melo

# A função é feita baseado em uma identificação de que é uma tupla de soma na função principal, por exemplo, T = ("+",R,S), sendo R = 1 e S = 0. Ou seja, T = ("+",1,0)
def er2afn_union(expreg):
    soma_dicio = dict()    # Criação de um dicionário para guardar as transições feitas através da função de soma 
    aut_inicio = set() # Criação de um set para guardar as transição do estado inicial 
    aut_final = set() # Criação de um set para guardar as transições ao estado final
    inicio = 0
    j = 1
    for i in expreg[1:]:  # For para percorrer os 2 simbolos 
        aut_inicio.add('q'+str(j))  # Adição dos estados ao set inicial 
        soma_dicio['q'+str(inicio),''] = {'q'+str(j)} 
        soma_dicio[('q'+str(j),i)] = {'q'+str(j+1)}
        aut_final.add('q'+str(j+1))  # Adição dos estados ao set final
        j += 2
    soma_dicio['q'+str(inicio),''] = aut_inicio 
    for f in aut_final:
        soma_dicio[f,''] = {'q'+str(j)}
    return soma_dicio




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


# Implementacao - 09 |Print de uma ER|
# @Lucas de Assumpcao Flores

def printw(expreg):
    operator = expreg[0]

    if len(expreg) == 3:
        if type(expreg[-2]) is tuple and type(expreg[-1]) is tuple:
            x1 = printw(expreg[-2])
            x2 = printw(expreg[-1])
            return "".join(str(x1) + str(operator) + str(x2))
        
        if type(expreg[-2]) is tuple:
            x1 = printw(expreg[-2])
            return "".join(str(x1) + str(operator) + str(expreg[-1]))

        if type(expreg[-1]) is tuple:
            x2 = printw(expreg[-1])
            return "".join(str(expreg[-2]) + str(operator) + str(x2))

        else:
            return "".join(str(expreg[-2]) + str(operator) + str(expreg[-1]))

    if len(expreg) == 2:
        if type(expreg[-1]) is tuple:
            x2 = printw(expreg[-1])
            return "".join(str(x2) + str(operator))
            
        else:    
            return "".join(str(expreg[-1]) + str(operator))

#Implementação 15
#@Ricardo Buçard de Castro

def afn2er_qi(automato, estado):
  estados_anteriores = set()
  indice = 0
  encontrado = False
  listaDelta = list(automato[2].values())
  for chave in automato[2]:
    if encontrado == False:
      estados_anteriores.add(chave[0])
      for estado_destino in listaDelta[indice]:
        if estado == estado_destino:
          encontrado = True
          break
      indice+=1
    else:
      break

# Implementação 16
# Dennis Santos Rodrigues


def afn2er_pi(automato, estado):
    values = list(automato[2].values())
    num = 0
    posterior = set()

    for funcao in automato[2]:
        if estado in funcao:
            for e in values[num]:
                if e != estado:
                 posterior.add(e)
        num += 1
    return posterior


# 13 - Transformação ER para AFN (4)
# Claudio Freitas
# Entrada [item1,item2, (item3, item4),...itemN]
def er2afn_kleene(expreg):
    afn = {}
    posAtual = 0
    while posAtual < len(expreg):
        posAtual = posAtual + 1
        estadoDePara = ('q' + str(posAtual -1), expreg[posAtual])
        nomeDoEstadoPara = ('q' + str(posAtual))
        afn[estadoDePara] = nomeDoEstadoPara
    i = 1
    for i in posAtual:
        if ('q' + str(i), 0) not in afn:
            afn[('q' + str(i), 0)] = 'q' + str(i)
        if ('q' + str(i), 1) not in afn:
            afn[('q' + str(i), 1)] = 'q' + str(i)
    return afn

# 14 - Transformacao ER para AFN (5)
# Claudio Freitas
# Entrada [item1,item2, (item3, item4),...itemN]
def er2afn(expreg):
    posAtual = 0
    while posAtual < len(expreg):
        atual = expreg[posAtual]
        posAtual = posAtual + 1
        if len(str(atual)) >= 2:
            if atual[0] == ' ' or atual[0] == 'epsilon':
               er2afn_base(expreg)
               break
            elif atual[0] == '+':
               er2afn_union('['+atual[0]+','+expreg[posAtual]+']')
            elif atual[0] == '*' and len(atual) > 2:
               er2afn_concat('['+atual[0]+','+expreg[posAtual]+']')
            elif atual[0] == "*" and len(atual) == 2:
               er2afn_kleene('['+atual[0]+','+expreg[posAtual]+']')
        else:
            if atual[0] == ' ' or atual[0] == 'epsilon':
               er2afn_base(expreg)
               break
            if atual == '+':
               er2afn_union('['+atual+','+expreg[posAtual]+']')
            elif atual == '*' and len(atual) > 2:
               er2afn_concat('['+atual+','+expreg[posAtual]+']')
            elif atual == "*" and len(atual) == 2:
               er2afn_kleene('['+atual+','+expreg[posAtual]+']')



# 17
# Dennis Rodrigues
def afn2er_rij(automato, estado, anterior, posterior):

    if estado != anterior and estado != posterior:
        values = list(automato[2].values())
        tuplas = []
        num = 0

        for funcao in automato[2]:
            if estado in funcao:
                for e in values[num]:
                    if e == posterior:
                        simbolo = funcao[1]
                        tuplas.append(tuple((anterior, simbolo)))
            num += 1

        return tuplas
    else:
        return 'O estado passado nao pode ser antecessor/posterior de si mesmo.'

