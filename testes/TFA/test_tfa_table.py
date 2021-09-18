import tc.prop_lr as prop_lr
import exemplos.afd_m1 as exp
import exemplos.prop_lr as prop_lr_exp
import modelos as modelos

def test_tfa_table():
    assert prop_lr.tfa_table(exp.M1) == \
        {
            ('q1', 'q2'): '',
            ('q1', 'q3'): '',
            ('q2', 'q3'): '',
        }
    assert prop_lr.tfa_table(prop_lr_exp.automato) == \
        {
            ('q0', 'q1'): '',
            ('q0', 'q2'): '',
            ('q0', 'q3'): '',
            ('q0', 'q4'): '',
            ('q0', 'q5'): '',
            ('q1', 'q2'): '',
            ('q1', 'q3'): '',
            ('q1', 'q4'): '',
            ('q1', 'q5'): '',
            ('q2', 'q3'): '',
            ('q2', 'q4'): '',
            ('q2', 'q5'): '',
            ('q3', 'q4'): '',
            ('q3', 'q5'): '',
            ('q4', 'q5'): ''
        }
    
    # Gustavo Pettine
    assert prop_lr.tfa_table(modelos.modelo1) == \
        {
            ('q1', 'q2'): '', 
            ('q1', 'q3'): '', 
            ('q2', 'q3'): ''
        }
    
    assert prop_lr.tfa_table(modelos.modelo2) == \
        {
            ('q0', 'q1'): '', 
            ('q0', 'q2'): '', 
            ('q1', 'q2'): ''
        }
