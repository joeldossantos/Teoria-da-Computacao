# Funções

def delta(automato, estado, simbolo, pilha):
    try:
        novo_estado, nova_pilha = automato[3][(estado, simbolo, pilha)]
        return novo_estado, nova_pilha
    except:
        return (None,None)


# (47) Implementação da função 'movimento' - Gustavo Pettine
def movimento(automato, palavra):
   
    if len(palavra) == 0:
        return {}

    estados, alfabeto_automato, alfabeto_pilha, transicoes, estado_atual, estado_atual_pilha, estado_final = automato

    resultado = {}
    chave = (estado_atual, palavra, estado_atual_pilha)

    simbolo_fita  = list(palavra).pop(0)
    simbolo_pilha = list(estado_atual_pilha).pop(0)

    novo_estado1,  nova_pilha1 = delta(automato, estado_atual, simbolo_fita, simbolo_pilha)
    novo_estado2,  nova_pilha2 = delta(automato, estado_atual, '', simbolo_pilha)

    if novo_estado1 is None and nova_pilha1 is None:
        resultado[chave] = {}
    
    else:

        if len(nova_pilha1) == 0:
            nova_pilha1 = [] if len(estado_atual_pilha) == 0 else list(estado_atual_pilha[1::])
        else:
            nova_pilha1 = nova_pilha1 + ([] if len(estado_atual_pilha) == 0 else list(estado_atual_pilha[1::]))

        nova_pilha1 = ''.join(nova_pilha1)

        novo_automato = (
            estados,
            alfabeto_automato,
            alfabeto_pilha,
            transicoes,
            novo_estado1,
            nova_pilha1,
            estado_final
        )
        resultado[chave] = movimento(novo_automato, palavra[1::])

    if novo_estado2 is not None and nova_pilha2 is not None:
        if len(nova_pilha2) == 0:
            nova_pilha2 = [] if len(estado_atual_pilha) == 0 else list(estado_atual_pilha[1::])
        else:
            nova_pilha2 = nova_pilha2 + ([] if len(estado_atual_pilha) == 0 else list(estado_atual_pilha[1::]))

        nova_pilha2 = ''.join(nova_pilha2)

        novo_automato = (
            estados,
            alfabeto_automato,
            alfabeto_pilha,
            transicoes,
            novo_estado2,
            nova_pilha2,
            estado_final
        )

        resultado |= movimento(novo_automato, palavra)

    return resultado


# (48) Implementação da função 'aceita' - Gustavo Pettine
def aceita(automato, palavra):

    return movimento(automato, palavra) in list(automato[6]) or len(palavra) == 0


# (49) Implementação da função 'computacao' - Gustavo Pettine
def computacao(automato, palavra):

    def printComputacao(chave, dicionario, historico=''):

        if len(dicionario.items()) > 0:
            chaves = list(dicionario[chave].keys())

            if len(chaves) > 0:
                for resultado in chaves:
                    if historico == '':
                        historico_aux = str(chave)

                    else:
                        historico_aux = historico + ' |- ' + str(chave)

                    printComputacao(resultado, dicionario[chave], historico_aux[::])

            else:
                print(historico + ' |- ' + str(chave))


    movimentos = movimento(automato, palavra)

    for resultado in list(movimentos.keys()):
        printComputacao(resultado, movimentos)
        print()


# Corrigindo os erros da função 'pn2pf' (extra) - Gustavo Pettine
def pn2pf(automato):

    novo_est_ini = 'p0'
    novo_est_fin = 'pf'
    pilha_start = "X0"
    dicio_pn2pf = {}

    pn2pf_estados = list(automato[0])
    carecteres = list(automato[1])
    caracteres_pilha = list(automato[2])
    dicio_origin = automato[3]
    pn_estado_ini = automato[4]
    pn_pilha_ini = automato[5]
    pn_estados_fin = list(automato[6])

    for caracter in range(len(carecteres)):
        dicio_pn2pf[(novo_est_ini, carecteres[caracter], pilha_start)] = (pn_estado_ini, [pn_pilha_ini, pilha_start])

        if (pn_estado_ini, carecteres[caracter], pn_pilha_ini) in dicio_origin:
            dicio_pn2pf[(pn_estado_ini, carecteres[caracter], pn_pilha_ini+pilha_start)] = dicio_origin[(pn_estado_ini, carecteres[caracter], pn_pilha_ini)]

    for estados in range(len(pn2pf_estados)):
        if (pn2pf_estados[estados], any(carecteres), any(caracteres_pilha)) in dicio_origin and pn2pf_estados[estados] is not pn_estado_ini:

            for caracter in range(len(carecteres)):
                if (pn2pf_estados[estados], carecteres[caracter], any(caracteres_pilha)) in dicio_origin:

                    for caracpilha in range(len(caracteres_pilha)):
                        if (pn2pf_estados[estados], carecteres[caracter], caracteres_pilha[caracpilha]) in dicio_origin:
                            dicio_pn2pf[(pn2pf_estados[estados], carecteres[caracter], caracteres_pilha[caracpilha])] = dicio_origin[(pn2pf_estados[estados], carecteres[caracter], caracteres_pilha[caracpilha])]


    for estado in range(len(pn_estados_fin)):
        dicio_pn2pf[(pn_estados_fin[estado], '', pn_pilha_ini)] = [(novo_est_fin, [])]

    caracteres_pilha.append(pilha_start)

    pn2pf_estados.append(novo_est_ini)
    pn2pf_estados.append(novo_est_fin)

    pf = (set(pn2pf_estados), set(carecteres), set(caracteres_pilha), dicio_pn2pf, novo_est_ini, pilha_start, {novo_est_fin})

    return pf

    