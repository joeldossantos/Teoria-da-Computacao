### Transformação de AF para GR

def gr2afn(automato):
    V = set()
    T = set()
    P = set()
    G = (V, T, P, S)
    for terminal in automato[0]:
        T.add(terminal)
    for estado in automato[2]:
        V.add(estado)
    for estado, terminal in automato[3]:
        P[estado] = [str(terminal), automato[3].value()]
    for final in automato[2]:
        P[final] = []
    S = automato[4]
