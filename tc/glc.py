### Transformação de AF para GR

   def afd2gr(automato):
    V = set()
    T = set()
    P = set()
    G = (V, T, P, S)
    indice = 0
    listaDelta = list(automato[3].values())
    for terminal in automato[0]:
        T.add(terminal)
    for estado in automato[2]:
        V.add(estado)
    for chave in automato[3]:
        P.add(str(chave[1]), listaDelta[indice])
        indice+=1
    for final in automato[2]:
        P.add(final, '')
    S = automato[4]
