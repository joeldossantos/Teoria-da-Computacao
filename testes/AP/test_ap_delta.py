import exemplos.ap as exp_ap
import tc.ap as ap

def test_ap_delta():
    assert ap.delta(exp_ap.M, 'q0', '1', 'X') == ('q1', ['X', 'X'])
    assert ap.delta(exp_ap.M, 'q0', '0', 'X') == ('q0', [])