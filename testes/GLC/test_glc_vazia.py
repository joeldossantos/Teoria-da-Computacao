#Testes feitos por Gabriel Lima de Souza em 2022

from tc import glc

def test_glc_vazia():

	# Teste 1
	assert glc.vazia(
		(
			{'S', 'A'},
			{'a','b'},
			{
				('S', ('a','S')),
				('S', ('b','S')),
				('S', ('A')),
				('A', ('a','a')),
				('A', ('b','b'))
			},
			'S'
		)
	)==("A GLC é vazia")
	# print(glc.vazia(
	# 	(
	# 		{'S', 'A'},
	# 		{'a','b'},
	# 		{
	# 			('S', ('a','S')),
	# 			('S', ('b','S')),
	# 			('S', ('A')),
	# 			('A', ('a','a')),
	# 			('A', ('b','b'))
	# 		},
	# 		'S'
	# 	)
	# ))

# 
#
#
#

	# Teste 2
	assert glc.vazia(
		(
			{'S', 'A'},
			{'a','b'},
			{
				('S', ('a','A')),
				('S', ('b','A')),
				('S', ('A')),
				('A', ('a','a')),
				('A', ('b','b'))
			},
			'S'
		)
	)
	# print(glc.vazia(
	# 	(
	# 		{'S', 'A'},
	# 		{'a','b'},
	# 		{
	# 			('S', ('a','A')),
	# 			('S', ('b','A')),
	# 			('S', ('A')),
	# 			('A', ('a','a')),
	# 			('A', ('b','b'))
	# 		},
	# 		'S'
	# 	)
	# ))

