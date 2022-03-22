# Exemplo 2.6 do slide de AFN, página 10 e 11


QSet = {'q0', 'q1', 'q2'}
Sigma = {1, 0}
Delta = {
    ('q0', 0): {'q0', 'q1'},
    ('q0', 1): {'q0'},
    ('q1', 1): {'q2'},
}
FSet = {'q2'}

automato = (QSet, Sigma, Delta, 'q0', FSet)
