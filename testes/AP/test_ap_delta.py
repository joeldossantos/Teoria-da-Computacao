import exemplos.ap as exp
import tc.ap as ap

def test_ap_delta():
    # (43) testanto a função 'delta' - Gustavo Pettine
    assert ap.delta(exp.M1, 'q0', '1', 'X') == ('q1', ['X', 'X']) #1
    assert ap.delta(exp.M1, 'q0', '0', 'X') == ('q0', []) #2
    assert ap.delta(exp.M2, 'q0', '1', 'Z') == ('q0', ['X', 'Z']) #3
    assert ap.delta(exp.M2, 'q0', '1', 'X') == ('q0', ['X', 'X']) #4
    assert ap.delta(exp.M2, 'q0', '', 'X') == ('q1', ['X']) #5
    assert ap.delta(exp.M2, 'q1', '0', 'X') == ('q1', []) #6
    assert ap.delta(exp.M3, 'q0', '1', 'X') == ('q1', ['X', 'X']) #7
    assert ap.delta(exp.M3, 'q1', '1', 'X') == ('q1', ['X', 'X']) #8
    assert ap.delta(exp.M3, 'q0', '0', 'X') == ('q0', []) #9
    assert ap.delta(exp.M3, 'q1', '0', 'X') == ('q0', []) #10