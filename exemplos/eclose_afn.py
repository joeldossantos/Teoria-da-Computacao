# Pode-se utilizar o dicionário abaixo como exemplo (Slide 16 de AFN) para testar a função de eclose presente em afn.py.

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
M1 = (QSet, Sigma, Delta, 'a', FSet)

 #print(eclose(M1,ESet))
