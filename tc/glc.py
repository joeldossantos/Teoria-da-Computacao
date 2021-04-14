### Transformação de AF para GR

def gr2afn(automato):
    V = set()
    T = set()
    P = set()
    R0 = set()
    G = (V, T, P, R0)
    for terminal in automato[0]:
        T.add(terminal)
    for estado in automato[2]:
        V.add(estado)
    for estado, terminal in automato[3]:
        P[estado] = [str(terminal), automato[3].value()]
    for final in automato[2]:
        P[final] = []
