'''
Testes unitários para as implementações
Rodar com "$pytest unit.py"
'''

import tc.afd as tc
import exemplos.afd_m1 as exp


def test_delta_hat():
    assert tc.delta_hat(exp.M1, 'q1', [1,1,0,1]) == 'q2'

def test_aceita():
    assert tc.aceita(exp.M1, [1,1,0,1])

def test_computacao():
    assert tc.computacao(exp.M1, 'q1', [1,1,0,1]) == "(q1, 1101) |- (q2, 101) |- (q2, 01) |- (q3, 1) |- (q2, )"
