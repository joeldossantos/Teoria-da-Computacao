import tc.afn as afn
import exemplos.afn_aceitacao as exp_aceitacao

def test_afn_delta_hat():
    assert afn.delta_hat(exp_aceitacao.automato, {'q0'}, [0]) == {'q0', 'q1'}
    assert afn.delta_hat(exp_aceitacao.automato, {'q0'}, [1]) == {'q0'}
    assert afn.delta_hat(exp_aceitacao.automato, {'q1'}, [1]) == {'q2'}
    assert afn.delta_hat(exp_aceitacao.automato, {'q1'}, [0]) == {None}