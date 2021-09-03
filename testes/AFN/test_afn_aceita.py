import tc.afn as afn
import exemplos.afn_aceitacao as exp_aceitacao

def test_afn_aceita():
    assert afn.aceita(exp_aceitacao.automato, [0]) == False
    assert afn.aceita(exp_aceitacao.automato, [1]) == False
    assert afn.aceita(exp_aceitacao.automato, [1,0]) == False
    assert afn.aceita(exp_aceitacao.automato, [0,1,0]) == False
    assert afn.aceita(exp_aceitacao.automato, [0,1]) == True
    assert afn.aceita(exp_aceitacao.automato, [1,0,1]) == True
    assert afn.aceita(exp_aceitacao.automato, [1,1,0,1]) == True
    assert afn.aceita(exp_aceitacao.automato, [0,1,0,1]) == True