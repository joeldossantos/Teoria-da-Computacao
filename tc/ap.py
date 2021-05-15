

def delta(automato, estado, simbolo, pilha):
    try:
        novo_estado, nova_pilha = automato[3][(estado, simbolo, pilha)]
        return novo_estado, nova_pilha
    except:
        return (None,None)

