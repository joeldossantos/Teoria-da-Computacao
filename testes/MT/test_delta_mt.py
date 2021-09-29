import tc.mt as mt
import exemplos.mt as mt_exp

def test_delta():

    assert mt.delta(mt_exp.M1,'q0','B') == ('q2','B','L')
    assert mt.delta(mt_exp.M1,'q1','1') == ('q1','0','R')
    assert mt.delta(mt_exp.M1,'q0','B') == ('q2','B','L')
    assert mt.delta(mt_exp.M1,'q2','B') == (None,None,None)
    assert mt.delta(mt_exp.M1,'q0','0') == ('q0', '1', 'R')

    assert mt.delta(mt_exp.M2,'q2','X') == ('q2', 'X', 'L')
    assert mt.delta(mt_exp.M2,'q4','0') == ('q5', '0', 'S')
    assert mt.delta(mt_exp.M2,'q5','B') == (None,None,None)
    assert mt.delta(mt_exp.M2,'q0','X') == ('q0', 'X', 'R')
    assert mt.delta(mt_exp.M2,'q1','1') == ('q1', '1', 'L')

    assert mt.delta(mt_exp.M3,'q10','Y') == ('q10', 'B', 'L')
    assert mt.delta(mt_exp.M3,'q6','B') == ('q8', 'B', 'R')
    assert mt.delta(mt_exp.M3,'q7','0') == ('q9', '0', 'R')
    assert mt.delta(mt_exp.M3,'q9','X') == ('q5', '1', 'R')
    assert mt.delta(mt_exp.M3,'q8','1') == (None,None,None)