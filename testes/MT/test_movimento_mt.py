import tc.mt as mt
import exemplos.mt as mt_exp

def test_movimento_mt():

    assert(mt.movimento(mt_exp.M1,'01')) == (['1', '0', 'B'])
    assert(mt.movimento(mt_exp.M1,'0110')) == (['1', '0', '0', '1', 'B'])
    assert(mt.movimento(mt_exp.M1,'1010')) == (['0', '1', '0', '1', 'B'])
    assert(mt.movimento(mt_exp.M1,'111111')) == (['0', '0', '0', '0', '0', '0', 'B'])
    assert(mt.movimento(mt_exp.M1,'00001')) == (['1', '1', '1', '1', '0', 'B'])
    assert(mt.movimento(mt_exp.M1,'11100010')) == (['0', '0', '0', '1', '1', '1', '0', '1', 'B'])
    assert(mt.movimento(mt_exp.M1,'01100110')) == (['1', '0', '0', '1', '1', '0', '0', '1', 'B'])
    assert(mt.movimento(mt_exp.M1,'0000000001000000')) == ([ '1',  '1',  '1',  '1',  '1',  '1',  '1',  '1',  '1', '0', '1',  '1',  '1',  '1',  '1',  '1', 'B'])
    assert(mt.movimento(mt_exp.M1,'10110110110111')) == (['0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0','B'])
    assert(mt.movimento(mt_exp.M1,'11101')) == (['0', '0', '0', '1', '0','B'])


    assert(mt.movimento(mt_exp.M2,'01')) == (['1', '0', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'0110')) == (['0', '1', '1', '0', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'1010')) == (['0', '1', '0', '1', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'111111')) == (['1', '1', '1', '1', '1', '1', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'00001')) == (['1', '0', '0', '0', '0', 'B', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'11100010')) == (['0', '1', '0', '0', '0', '1', '1', '1', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'01100110')) == (['0', '1', '1', '0', '0', '1', '1', '0', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'0000000001000000')) == ([ '0',  '0',  '0',  '0',  '0',  '0',  '1',  '0',  '0', '0', '0',  '0',  '0',  '0',  '0',  '0', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'10110110110111')) == (['1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
    assert(mt.movimento(mt_exp.M2,'11101')) == (['1', '0', '1', '1', '1', 'B', 'B', 'B', 'B', 'B', 'B'])
