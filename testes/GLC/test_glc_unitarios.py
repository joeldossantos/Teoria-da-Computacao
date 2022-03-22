from tc import glc_add


#  S -> aXa | bXb
#  X -> a | b | S | e

Vp = {'S','X'}
Tp = {'a','b'}
Pp = {('S',('a','X','a')),
	('S',('b','X','b')),
	('X',('a')),
	('X',('b')),
	('X',('S')),
	('X',())}

G = (Vp,Tp,Pp,'S')


V1 = {'S','A','B','C','D'}
T1 = {'a','b','c'}
P1 = {('S',('A')),
	('S',('A','A')),
	('A',('S')),
	('A',('B')),
	('B',('C')),
	('B',('a')),
	('B',('CC')),
	('C',('D')),
	('C',('b')),
	('D',('c'))}

G2 = (V1,T1,P1,'S')


def test_unitarios():
    assert glc_add.unitarios(G) == {('X', 'X'), ('X', 'S'), ('S', 'S')}