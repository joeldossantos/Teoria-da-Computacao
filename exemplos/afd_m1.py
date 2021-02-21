'''
Exemplo M1, AFD - slide 10
'''

import tc.afd as tc


Sigma = {'0', '1'}
QSet = {'q1', 'q2', 'q3'}
FSet = {'q2'}
Delta = {
            ('q1', 0): 'q1',
            ('q1', 1): 'q2',
            ('q2', 0): 'q3',
            ('q2', 1): 'q2',
            ('q3', 0): 'q2',
            ('q3', 1): 'q2'
        }

M1 = (QSet, Sigma, Delta, 'q1', FSet)