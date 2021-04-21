'''
Testes unitários para as implementações
pip install pytest
Rodar com "$pytest unit.py"
Windows: py -m pytest unit.py
'''

import exemplos.eclose_afn as exp_eclose
import exemplos.afn_aceitacao as exp_aceitacao
import exemplos.prop_lr as prop_lr_exp
import tc.afd as tc
import tc.afn as afn
import tc.prop_lr as prop_lr
import exemplos.afd_m1 as exp


def test_delta_hat():
    assert tc.delta_hat(exp.M1, 'q1', [1,1,0,1]) == 'q2'

def test_aceita():
    assert tc.aceita(exp.M1, [1,1,0,1])

def test_computacao():
    assert tc.computacao(exp.M1, 'q1', [1,1,0,1]) == "(q1, 1101) |- (q2, 101) |- (q2, 01) |- (q3, 1) |- (q2, )"
    assert tc.computacao(exp.M1, 'q1', [1,1,0,1,1]) == "(q1, 11011) |- (q2, 1011) |- (q2, 011) |- (q3, 11) |- (q2, 1) |- (q2, )"
    assert tc.computacao(exp.M1, 'q1', [1,1,0]) == "(q1, 110) |- (q2, 10) |- (q2, 0) |- (q3, )"

def test_afn_eclose():
    assert afn.eclose(exp_eclose.M1, {'a'}) == {'b', 'e', 'c', 'a', 'd'}
    assert afn.eclose(exp_eclose.M1, {'b'}) == {'b', 'c', 'd'}
    assert afn.eclose(exp_eclose.M1, {'f'}) == {'f', 'g'}
    assert afn.eclose(exp_eclose.M1, {'g'}) == {'g'}
    assert afn.eclose(exp_aceitacao.automato, {'q0'}) == {'q0'}
    assert afn.eclose(exp_aceitacao.automato, {'q1'}) == {'q1'}

def test_afn_delta_hat():
    assert afn.delta_hat(exp_aceitacao.automato, {'q0'}, [0]) == {'q0', 'q1'}
    assert afn.delta_hat(exp_aceitacao.automato, {'q0'}, [1]) == {'q0'}
    assert afn.delta_hat(exp_aceitacao.automato, {'q1'}, [1]) == {'q2'}
    assert afn.delta_hat(exp_aceitacao.automato, {'q1'}, [0]) == set() # @Conrado Luiz set vazio. i.e. {}. Só a notação em python que é estranha

def test_afn_aceita():
    assert afn.aceita(exp_aceitacao.automato, [0]) == False
    assert afn.aceita(exp_aceitacao.automato, [1]) == False
    assert afn.aceita(exp_aceitacao.automato, [1,0]) == False
    assert afn.aceita(exp_aceitacao.automato, [0,1,0]) == False
    assert afn.aceita(exp_aceitacao.automato, [0,1]) == True
    assert afn.aceita(exp_aceitacao.automato, [1,0,1]) == True
    assert afn.aceita(exp_aceitacao.automato, [1,1,0,1]) == True
    assert afn.aceita(exp_aceitacao.automato, [0,1,0,1]) == True

def test_tfa_table():
    assert prop_lr.tfa_table(exp.M1) == \
        [
            ['q1', 'q2', ''],
            ['q1', 'q3', ''],
            ['q2', 'q3', ''],
        ]
    assert prop_lr.tfa_table(prop_lr_exp.automato) == \
        [
            ['q0', 'q1', ''],
            ['q0', 'q2', ''],
            ['q0', 'q3', ''],
            ['q0', 'q4', ''],
            ['q0', 'q5', ''],
            ['q1', 'q2', ''],
            ['q1', 'q3', ''],
            ['q1', 'q4', ''],
            ['q1', 'q5', ''],
            ['q2', 'q3', ''],
            ['q2', 'q4', ''],
            ['q2', 'q5', ''],
            ['q3', 'q4', ''],
            ['q3', 'q5', ''],
            ['q4', 'q5', '']
        ]