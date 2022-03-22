# SLIDE: PROPRIEDADES DAS LR - PAGINA 37

Sigma = {'a', 'b'}
QSet = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
FSet = {'q0', 'q4', 'q5'}
Delta = {
            ('q0', 'a'): 'q2',
            ('q0', 'b'): 'q1',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q0',
            ('q2', 'a'): 'q4',
            ('q2', 'b'): 'q5',
            ('q3', 'a'): 'q5',
            ('q3', 'b'): 'q4',
            ('q4', 'a'): 'q3',
            ('q4', 'b'): 'q2',
            ('q5', 'a'): 'q2',
            ('q5', 'b'): 'q3'
        }

automato = (QSet, Sigma, Delta, 'q0', FSet)