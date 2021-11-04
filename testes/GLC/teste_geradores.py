import tc.glc as glc

#ALUNO : ADEOYE SUNDAY LADELE 
#TESTE DA FUNCAO GERADORES()
#IMPLEMENTACAO 66

V = {'E', 'I'}
T = {'+', '*', '-', '(', ')', 'a', 'b', '0', '1'}
P = {('E', ('I')),
     ('E', ('E', '+', 'E')),
     ('E', ('E', '*', 'E')),
     ('E', ('E', '-', 'E')),
     ('E', ('(', 'E', ')')),
     ('I', ('a')),
     ('I', ('b')),
     ('I', ('I', 'a')),
     ('I', ('I', 'b')),
     ('I', (0)),
     ('I', (1))
     }
G = (V, T, P, 'E')
A = {'S','T','C'}
B = {'a','b'}
C = {('S',('aS')),
    ('S',()),
    ('S',('a','T')),
    ('S',('a','C')),
     ('T',('b','T')),
     ('T',()),
    }
M = (A,B,C,'S')

def test_gerador():
    assert glc.geradores(G) == {'E','I','+', '*', '-', '(', ')', 'a', 'b', '0', '1'}
    assert glc.geradores(M) == {'S','T','a','b'}
