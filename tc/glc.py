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
