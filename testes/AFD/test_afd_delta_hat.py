import tc.afd as tc
import exemplos.afd_m1 as exp

def test_delta_hat():
    assert tc.delta_hat(exp.M1, 'q1', [1,1,0,1]) == 'q2'
