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
    assert tc.computacao(exp.M1, 'q1', [1,1,0,1,1]) == "(q1, 11011) |- (q2, 1011) |- (q2, 011) |- (q3, 11) |- (q2, 1) |- (q2, )"
    assert tc.computacao(exp.M1, 'q1', [1,1,0]) == "(q1, 110) |- (q2, 10) |- (q2, 0) |- (q3, )"