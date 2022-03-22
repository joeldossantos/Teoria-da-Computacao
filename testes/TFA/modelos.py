# Gustavo Pettine

Sigma = {0, 1}
QSet = {'q1', 'q2', 'q3'}
FSet = {'q3'}
Delta = {
            ('q1', 0): 'q1',
            ('q1', 1): 'q2',
            ('q2', 0): 'q3',
            ('q2', 1): 'q2',
            ('q3', 0): 'q2',
            ('q3', 1): 'q2'
        }

modelo1 = (QSet, Sigma, Delta, 'q1', FSet)

Sigma = {0, 1}
QSet = {'q0', 'q1', 'q2'}
FSet = {'q2'}
Delta = {
            ('q0', 0): 'q1',
            ('q1', 0): 'q2',
            ('q2', 0): 'q2',
            ('q2', 1): 'q2'
        }

modelo2 = (QSet, Sigma, Delta, 'q0', FSet)

Sigma = {0, 1}
QSet = {'q0', 'q1', 'q2', 'q3'}
FSet = {'q3'}
Delta = {
            ('q0', 0): 'q0',
            ('q0', 1): 'q1',
            ('q1', 0): 'q1',
            ('q1', 1): 'q2',
            ('q2', 1): 'q3'
        }

modelo3 = (QSet, Sigma, Delta, 'q0', FSet)