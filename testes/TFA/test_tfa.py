import exemplos.prop_lr as prop_lr_exp
import tc.prop_lr as prop_lr
import exemplos.afd_m1 as exp
import modelos as modelos

# Gustavo Pettine

def test_tfa():

    assert prop_lr.tfa(exp.M1) == {('q1', 'q3')}

    assert prop_lr.tfa(prop_lr_exp.automato) == {('q2', 'q3'), ('q4', 'q5')}

    # Gustavo Pettine
    assert prop_lr.tfa(modelos.modelo1) == set()

    assert prop_lr.tfa(modelos.modelo2) == set()