#10 Transformação ER para AFN (1)
#Lucas Sargeiro Gomes de Mello

# A função recebe um símbolo e monta o autômato base para aquele símbolo
#
#             	{None}	= (i) --None--> (f)
#	            None	= (i)     		(f)
#	            {a}		= (i) ---a----> (f)
#

count_i = 0     # Contador usado para gerar os nomes dos estados
def er2afn_base(simbolo):
    global count_i
    count_i += 1

    if simbolo == None:
        QSet = {f'i{count_i}', f'f{count_i}'}
        Sigma = {}
        Delta = {}
        FSet = {f'f{count_i}'}

        return (QSet, Sigma, Delta, f'i{count_i}', FSet)
    
    elif simbolo == '':
        QSet = {f'i{count_i}', f'f{count_i}'}
        Sigma = {}
        Delta = {
            (f'i{count_i}', ''):{f'f{count_i}'}
        }
        FSet = {f'f{count_i}'}
        return (QSet, Sigma, Delta, f'i{count_i}', FSet)

    else:
        QSet = {f'i{count_i}', f'f{count_i}'}
        Sigma = {simbolo}
        Delta = {
            (f'i{count_i}', simbolo):{f'f{count_i}'}
        }
        FSet = {f'f{count_i}'}

        return (QSet, Sigma, Delta, f'i{count_i}', FSet)

#11 Transformação ER para AFN (2)
# Lucas Sargeiro Gomes de Mello

#A funcao é baseada em  2 automatos R e S, usando o padrão (QSet, Sigma, Delta, EstadoInicial, FSet)
#
#				    --None-->   (iR)--->[R]--->(fR)   --None--
#				   /			        		              \
#	R+S 	=  (i)-				         		               >(f)
#				   \                                          /
#				   	--None-->   (iS)--->[S]--->(fS)   --None--
#
#	O AFN chega ao estado final seja pelo automato R ou pelo automato S.
# 
#    PASSOS:
#
#		- Cria um novo estado inicial com transicao vazia para
#		o estado inicial de cada automato.
#
#		- Cria um novo estado final que recebe transicao vazia
#		de cada estado final antigo.

def er2afn_union(R, S):
    global count_i

    count_i += 1
    new_i = f'i{count_i}'
    new_f = f'f{count_i}'
    
    newQSet = R[0].union(S[0]).union({new_i, new_f})
    newSigma = R[1].union(S[1])
    
    end_R = next(iter(R[4]))
    end_S = next(iter(S[4]))

    newDelta = {
        (new_i, ''):{R[3], S[3]},
        (end_R, ''):{new_f},
        (end_S, ''):{new_f},
        **R[2],
        **S[2]
    }
    newFSet = {new_f}

    return (newQSet, newSigma, newDelta, new_i, newFSet)




#12 Transformação ER para AFN (3)
#Lucas Sargeiro Gomes de Mello

#A funcao é baseada em  2 automatos R e S, usando o padrão (QSet, Sigma, Delta, EstadoInicial, FSet)
#
#	RS 		=  (i)-->[R]-->(fR)   --None-->   (iS)-->[S]-->(f)
#	
#	O AFN chega ao estado final apos passar pelos automatos R e depois S.
#
#   PASSOS:
#
#		- O estado inicial do primeiro vira estado inicial do 
#		automato.
#
#		- O estado final do primeiro se liga ao estado inicial
#		do segundo com transicao vazia.
#
#		- O estado final do segundo vira estado final do automato.
#

def er2afn_concat(R, S):
    newQSet = R[0].union(S[0])
    newSigma = R[1].union(S[1])
    
    end_R = next(iter(R[4]))

    newDelta = {
        **R[2],
        (end_R, ''): {S[3]},
        **S[2]
    }
    newFSet = S[4]

    return (newQSet, newSigma, newDelta, R[3], newFSet)


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
    return estados_anteriores

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
# Lucas Sargeiro Gomes de Mello

#A funcao é baseada em  2 automatos R e S, usando o padrão (QSet, Sigma, Delta, EstadoInicial, FSet)
#
#                               --- None
#							  /     \
#                            v       \
#	R*		=  (i)--None-->[     R     ]--None-->(f)
#			    |                                 ^
#			    ----------------------------------'
#
#	O AFN chega ai estado final sem ler nada, ou repetindo a leitura
#	feita pelo automato R n vezes.
#   
#   PASSOS:
#           
#		- Criar um novo estado inicial que tem transição vazia para
#		o antigo estado inicial do autômato.
#
#		- Criar uma transicao para antigo estado final do automato
#		levando para um novo estado final do automato, com transicao
#       vazia.
#
#		- Criar uma transicao vazia do antigo estado final para o antigo
#       estado inicial.
#
#       - Criar uma transicao do novo estado inicial para o novo estado
#       final do automato.
#
def er2afn_kleene(R):
    global count_i

    count_i += 1
    new_i = f'i{count_i}'
    new_f = f'f{count_i}'
    
    newQSet = R[0].union({new_i, new_f})
    newSigma = R[1]
    
    end_R = next(iter(R[4]))

    newDelta = {
        (new_i, ''):{R[3], new_f},
        (end_R, ''):{new_f, R[3]},
        **R[2]
    }
    newFSet = {new_f}

    return (newQSet, newSigma, newDelta, new_i, newFSet)


# 14 - Transformacao ER para AFN (5)
# Lucas Sargeiro Gomes de Mellos

# A função recebe uma expressão regular na forma de tupla utilizando a notação pré fixada
#    
#                       ('operador', 'operando1' | ER , ['operando2' | ER])
# Exemplos:
#              ('+', 1, 0)      --> união
#              ('', 'a', 'b')   --> concatenação
#              ('*', 'a')       --> fecho kleene

def er2afn(expreg):
    operador = expreg[0]                            # Obtem o primeiro operador

    operando_1 = expreg[1]                          # Obtem o primeiro parametro, que pode ser um operando
                                                    # ou uma outra expressão regular (ER)
    if type(operando_1) is tuple:                   
        operando_1 = er2afn(operando_1)             # Caso seja uma outra ER, chama a função recursivamente
    else:
        operando_1 = er2afn_base(operando_1)        # Caso não, busca o automato base para o simbolo
    
    if len(expreg) > 2:                             # Como o segundo parâmetro é opcional, é preciso saber
        operando_2 = expreg[2]                      # se ele existe antes de buscar seu valr
        if type(operando_2) is tuple:
            operando_2 = er2afn(operando_2)
        else:
            operando_2 = er2afn_base(operando_2)

    if operador == '+':                             # Para cada operador a função correspondente é chamada
        return er2afn_union(operando_1, operando_2)
    elif operador == '':
        return er2afn_concat(operando_1, operando_2)
    elif operador == '*':
        return er2afn_kleene(operando_1)



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
                        #tuplas.append(simbolo)
            num += 1

        return tuplas
    else:
        return 'O estado passado nao pode ser antecessor/posterior de si mesmo.'

#Implementacao 18
#@Pedro Henrique Gomes Telles
def afn2er_s(automato, estado):
    anteriores = afn2er_qi(automato, estado)
    posteriores = afn2er_pi(automato, estado)
    
    for ant in anteriores:
        if estado != ant:
            for pos in posteriores:
                if estado != pos:
                    automato[2][afn2er_rij(automato, estado, ant, pos)[0]] = {pos}
    automato[0].remove(estado)
    for k, v in list(automato[2].items()):
        if estado in k:
            automato[2].pop(k)
        if estado == v:
            automato[2].pop(k)
    return automato[2]

#Implementação 19
#@Pedro Henrique Gomes Telles
def afn2er(automato):
    estado_ini = automato[3]
    estado_fim = automato[4]
    automato_aux = automato[0]
    for estado in automato_aux:
        if estado != estado_ini and estado != estado_fim:
            afn2er_s(automato, estado)
    
    if estado_ini not in automato[2].items():
        expreg = automato[2][(estado_ini, 0)]

    if estado_ini in automato[2].items():
        expreg = ('*', automato[2][(estado_ini, 0)])

    if estado_fim in automato[2].items():
        expreg += (('*', automato[2][(estado_ini, 0)]))

    return expreg
