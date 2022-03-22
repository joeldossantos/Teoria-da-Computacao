#Implementação 03
#Author: Diego Cortinhas

import tc.afn as tc
#Parametros de teste para Automato01
QSet = {'q0', 'q1', 'q2','q3'}
Sigma = {1, 0}
Delta = {
    ('q0', 0): {'q0'},
    ('q0', 1): {'q0', 'q1'},
    ('q1', 0): {'q1'},
    ('q1', 1): {'q1','q2'},
    ('q2', 0): {'q2'},
    ('q2', 1): {'q2','q3'},
    ('q3', 0): {'q3'},
    ('q3', 1): {'q3'}

}
Delta_eclose = {
    ('q0',''): {'q0', 'q1', 'q2','q3'},
    ('q1',''): {'q1','q2'},
    ('q2',''): {'q2'},
    ('q3',''): {'q3'},
    ('q3',0): {'q3'},
    ('q3',1): {'q3'}
}
FSet = {'q3'}

#Parametros de teste para Automato02
QSet2 = {'q0', 'q1', 'q2'}
Delta2 = {
    ('q0', 0): {'q0'},
    ('q0', 1): {'q0', 'q1'},
    ('q1', 0): {'q1'},
    ('q1', 1): {'q1','q2'},
    ('q2', 0): {'q2'},
    ('q2', 1): {'q2'}
}

Delta_eclose2 = {
    ('q0',''): {'q0', 'q1', 'q2'},
    ('q1',''): {'q1','q2'},
    ('q2',''): {'q2'},
    ('q2',0): {'q2'},
    ('q2',1): {'q2'}
}
FSet2 = {'q2'}


#Automato01
A1 = (QSet, Sigma, Delta, 'q0', FSet)
#Palavra de Teste para automato 01
t1 = [0,1,0,1,1,1,1]

#Automato02
A2 = (QSet2, Sigma, Delta2, 'q0', FSet2)
#Palavra de Teste para automato 02
t2 = [1,1,1,1,1]

def test_afn_aceita():
    #testeAutomato01
    assert tc.aceita(A1,t1) == 'true'
    #testeAutomato02
    assert tc.aceita(A2,t2) == 'true'

def test_afn_delta():
    #testeAutomato01
    assert tc.delta(A1,'q0',0) == 'q0'
    #testeAutomato02
    assert tc.delta(A2,'q0',0) == 'q0'

def test_afn_delta_hat():
    #testeAutomato01
    assert tc.delta_hat(A1,{'q0'}, [0]) == {'q0'}
    assert tc.delta_hat(A1,{'q0'}, [1]) == {'q0', 'q1'}
    #testeAutomato02
    assert tc.delta_hat(A2,{'q0'}, [0]) == {'q0'}
    assert tc.delta_hat(A2,{'q0'}, [1]) == {'q0', 'q1'}

def test_afn_eclose():
    #testeAutomato01
    assert tc.eclose(Delta_eclose, {'q0'}) == {'q0', 'q1', 'q2','q3'}
    assert tc.eclose(Delta_eclose, {'q1'}) == {'q1', 'q2'}
    assert tc.eclose(Delta,{'q0'}) == {'q0'}
    assert tc.eclose(Delta,{'q1'}) == {'q1'}
    #testeAutomato02
    assert tc.eclose(Delta_eclose2, {'q0'}) == {'q0', 'q1', 'q2'}
    assert tc.eclose(Delta_eclose2, {'q1'}) == {'q1', 'q2'}
    assert tc.eclose(Delta2,{'q0'}) == {'q0'}
    assert tc.eclose(Delta2,{'q1'}) == {'q1'}


def main (args):
    print(test_afn_delta_hat())
    print(test_afn_delta())
    print(test_afn_aceita())
    print(test_afn_eclose())
    
    ##############Testes Automato 01##################
    #Função delta_hat testada(A1,'q0',t1)
    print(tc.delta_hat(A1,'q0',t1))
    
    #Função delta testada 
    # Recebendo simbolo 1 
    proxSimbolo1 = tc.delta(A1,'q0',1)
    print(proxSimbolo1)
    
    # Recebendo simbolo 1 novamente
    proxSimbolo2 = tc.delta(A1,proxSimbolo1,1)
    print(proxSimbolo2)
    
    #Função aceita testada(A1,t1)
    aceita = tc.aceita(A1,t1)
    print(aceita)

    #Funcao eclose testada(Automato,Estados)
    eclose = tc.eclose(A1,{'q0', 'q1', 'q2','q3'})
    print(eclose)


    ##############Testes Automato 02##################
    #Função delta_hat testada(A2,'q0',t2)
    print(tc.delta_hat(A2,'q0',t2))
    
    #Função delta testada 
    # Recebendo simbolo 1 
    proxSimbolo1_automato2 = tc.delta(A2,'q0',1)
    print(proxSimbolo1_automato2)
    
    # Recebendo simbolo 1 novamente
    proxSimbolo2_automato2 = tc.delta(A2,proxSimbolo1_automato2,1)
    print(proxSimbolo2_automato2)
    
    #Função aceita testada(A1,t1)
    aceita_automato2 = tc.aceita(A2,t2)
    print(aceita_automato2)

    #Funcao eclose testada(Automato,Estados)
    eclose_automato2 = tc.eclose(A2,{'q0', 'q1', 'q2'})
    print(eclose_automato2)

    return
