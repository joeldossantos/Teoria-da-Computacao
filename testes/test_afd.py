#Implementação 01 
#Author: Diego Cortinhas

import tc.afd as tc

# simbolo a - avanca para proximo estado
# simbolo v - volta para estado anterior
# simbolo p - permanece naquele estado

Sigma = {'a', 'v','p'}
Estados = {'q1', 'q2', 'q3'}
Final = {'q1'}

Delta = {
            ('q1', 'v'): 'q1',
            ('q1', 'p'): 'q1',
            ('q1', 'a'): 'q2',
            ('q2', 'v'): 'q1',
            ('q2', 'p'): 'q2',
            ('q2', 'a'): 'q3',
            ('q3', 'v'): 'q2',
            ('q3', 'p'): 'q3',
            ('q3', 'a'): 'q3',
        }

A1 = (Estados, Sigma, Delta, 'q1', Final)
t1 = ['a','a','p','p','v','p','v']

def test_delta_hat():
    assert tc.delta_hat(A1,'q1',t1) == 'q1'

def test_delta():
    assert tc.delta(A1,'q1','a') == 'q2'

def test_aceita():
    assert tc.aceita(A1,t1)

def test_computacao():
    assert computacao(A1, 'q1', t1) == "(q1, aappvpv) |- (q2, appvpv) |- (q3, ppvpv) |- (q3, pvpv) |- (q3, vpv) |- (q2, pv) |- (q2, v) |- (q1, )"
 
def main (args):
    print(test_delta_hat())
    print(test_delta())
    print(test_aceita())
    print(test_computacao())
    
    #Função delta hat testada(A1,'q1',t1)
    print(tc.delta_hat(A1,'q1',t1))
    
    #Função delta testada 
    # Recebendo simbolo a - avancando para proximo simbolo q2
    proxSimbolo1 = tc.delta(A1,'q1','a')
    print(proxSimbolo1)
    
    # Recebendo simbolo a - avancando para proximo simbolo q3
    proxSimbolo2 = tc.delta(A1,proxSimbolo1,'a')
    print(proxSimbolo2)
    
    #Função aceita testada(A1,t1)
    aceita = tc.aceita(A1,t1)

    #Funcao computacao testada(A1, 'q1', t1)
    config = tc.computacao(A1, 'q1', t1)
    print(config)

    return

    
