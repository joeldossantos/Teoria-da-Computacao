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




def test_remove_unitarias():
    assert glc_add.remove_unitarias(G) == ({'S', 'X'}, {'b', 'a'}, {('X', 'a'), ('S', ('a', 'X', 'a')), ('S', ('b', 'X', 'b')), ('X', ('b', 'X', 'b')), ('X', ('a', 'X', 'a')), ('X', 'b'), ('X', ())}, 'S')


