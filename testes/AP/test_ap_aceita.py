import exemplos.ap as exp
import tc.ap as ap

def test_ap_aceita():
# (78) testando a função 'aceita' - Gustavo Pettine
  assert ap.aceita(exp.M2, '') == True
  assert ap.aceita(exp.M2, '11001') == False