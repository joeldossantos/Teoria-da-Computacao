

def delta(automato, estado, simbolo, pilha):
    try:
        novo_estado, nova_pilha = automato[3][(estado, simbolo, pilha)]
        return novo_estado, nova_pilha
    except:
        return (None,None)

#51 Transformação Pilha Vazia para Estado Final
#Criar uma função que transforma um AP que aceita por pilha vazia para um equivalente
#que aceita por estado final. A transformação deverá seguir o algoritmo apresentado em
#aula.
#Atenção:
# A assinatura da função deverá ser pn2pf(automato).
# Essa função deverá ser criada no arquivo (ap.py).

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

    for caracter in caracteres:
        dicio_pn2pf[(novo_est_ini, caracteres[caracter], pilha_start)] = (pn_estado_ini, [pn_pilha_ini, pilha_start])

        if (pn_estado_ini, carecteres[caracter], pn_pilha_ini) in dicio_origin:
            dicio_pn2pf[(pn_estado_ini, carecteres[caracter], pn_pilha_ini+pilha_start)] = dicio_origin[(pn_estado_ini, carecteres[caracter], pn_pilha_ini)]

    for estados in pn2pf_estados:
        if (pn2pf_estados[estados], any(caracteres), any(caracteres_pilha)) in dicio_origin and pn2pf_estados[estados] is not pn_estado_ini_ini:

            for caracter in caracteres:
                if (pn2pf_estados[estados], caracteres[caracter], any(caracteres_pilha)) in dicio_origin:

                    for caracpilha in caracteres_pilha:
                        if (pn2pf_estados[estados], caracteres[caracter], caracteres_pilha[caracpilha]) in dicio_origin:
                            dicio_pn2pf[(pn2pf_estados[estados], caracteres[caracter], caracteres_pilha[caracpilha])] = dicio_origin[(pn2pf_estados[estados], caracteres[caracter], caracteres_pilha[caracpilha])]


    for estado in pn_estados_fin:
        dicio_pn2pf[(pn_estados_fin[estado], [], pn_pilha_ini)] = [(novo_est_fin, [])]

    caracteres_pilha.append(pilha_start)

    pn2pf_estados.append(novo_est_ini)
    pn2pf_estados.append(novo_est_fin)

    pf = (pn2pf_estados, caracteres, caracteres_pilha, dicio_pn2pf, novo_est_ini, pilha_start, {novo_est_fin})

    return pf
