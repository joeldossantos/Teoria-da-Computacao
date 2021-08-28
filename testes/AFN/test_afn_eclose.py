import tc.afn as afn
import exemplos.eclose_afn as exp_eclose
import exemplos.afn_aceitacao as exp_aceitacao

def test_afn_eclose():
    assert afn.eclose(exp_eclose.M1, {'a'}) == {'b', 'e', 'c', 'a', 'd'}
    assert afn.eclose(exp_eclose.M1, {'b'}) == {'b', 'c', 'd'}
    assert afn.eclose(exp_eclose.M1, {'f'}) == {'f', 'g'}
    assert afn.eclose(exp_eclose.M1, {'g'}) == {'g'}
    assert afn.eclose(exp_aceitacao.automato, {'q0'}) == {'q0'}
    assert afn.eclose(exp_aceitacao.automato, {'q1'}) == {'q1'}