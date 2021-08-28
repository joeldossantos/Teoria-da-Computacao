import tc.mt as mt
import exemplos.mt as mt_exp



def test_mt_computacao_com_parada():
    assert mt.computacaoComParada(mt_exp.M1, mt_exp.palavra) == ('0101001', True)
    assert mt.computacaoComParada(mt_exp.M1, mt_exp.palavra) != ('0101000', True)

    assert mt.computacaoComParada(mt_exp.M2, mt_exp.palavra) == ('0110101', True)
    assert mt.computacaoComParada(mt_exp.M2, mt_exp.palavra) != ('0101000', True)

    assert mt.computacaoComParada(mt_exp.M3, mt_exp.palavra) == ('0110101', True)
    assert mt.computacaoComParada(mt_exp.M3, mt_exp.palavra) != ('0101000', True)