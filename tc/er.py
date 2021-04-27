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
            return "".join(str(expreg[-2]) + str(operator) + str(expreg[-1]))
        
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
  listaDelta = list(automato[3].values())
  for chave in automato[3]:
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
        if estado in funcao and values[num] != estado:
            posterior.add(values[num])
        num += 1
    return posterior
