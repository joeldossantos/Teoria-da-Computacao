'''
Autômato Finito Não Determinístico (AFN)
'''
# 2 - delta do AFN
def delta(automato, estado, simbolo):
    return automato[2][(estado, simbolo)]

# o retorno é uma lista de estados
# passando referencia da lista ao inves de valor string. A diferença no AFN ocorre  quando ele esta entrando no estado (o que ainda nao é esse parte)

# 3 - Fecho-Epsilon
# A função eclose pode receber um estado com apenas um elemento (Set1 = 'a') ou um conjunto de elementos (Set2 = 'a','b','c','d').
def eclose(automato,estado):
    simbolo = ''   # O simbolo possui valor '' para definir como se fosse um épsilon.
    eclosure = set()   # Nesta linha foi criado um set vazio eclosure = { }
    for estados in estado:   # Este for serve para percorrer cada estado presente no Set de entrada(estado), seja eles Set1 ou Set2, por exemplo.
        eclosure = eclosure.union(delta(automato, estados, simbolo))  # Nesta linha o eclosure está utilizando o .union para somar o eclose de cada elemento do set de entrada e guardar na própria variável.
    return eclosure # Será retornado um Set com o resultado da soma do eclose de cada Set de entrada.

# Pode-se utilizar o dicionário abaixo como exemplo (Slide 16 de AFN)
"""
Sigma = {'x', 'y'}
QSet = {'a', 'b', 'c','d','e','f','g'}
ESet = {'c','d','g'} # ESet não faz parte do exemplo do slide, é apenas um Set criado para utilizar como exemplo de entrada.
FSet = {'g'}
Delta = {
            ('a',''): {'a','b','c','d','e'},
            ('b',''): {'b','c','d'},
            ('c',''): {'c','d'},
            ('d',''): {'d'},
            ('e',''): {'e'},
            ('e','x'): {'f'},
            ('f',''): {'f','g'},
            ('f','y'): {'d'},
            ('g',''): {'g'},
 }

M1 = (QSet, Sigma, Delta, 'q1', FSet)
"""
# print(eclose(M1,ESet))
