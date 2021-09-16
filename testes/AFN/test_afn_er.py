from tc.er import afn2er_pi, afn2er_qi, afn2er_rij, afn2er_s, afn2er
from exemplos.afn_aceitacao import automato

# Implementação 11 - Diogo Alves da Silva

def test_afn2er_qi():
    assert afn2er_qi(automato, "q2") == {'q0', 'q1'}

def test_afn2er_pi():
    assert afn2er_pi(automato, "q1") == {'q2'}

def test_afn2er_rij():
    assert afn2er_rij(automato, "q1", "q0", "q2") == [('q0', 1)]

def test_afn2er_s():
    assert afn2er_s(automato, "q0") == {('q1', 1): {'q2'}}