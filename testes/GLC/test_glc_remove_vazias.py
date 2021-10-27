import tc.glc as glc

# Implementação de testes da remove_vazias (tarefa 32)
# Aluno: Diogo Alves da Silva

def test_remove_vazias():
    gramatica_a = ({'X'}, 
            {'a', '+', '*'}, 
            {('X', ('X', '+', 'X')), ('X', ('X', '*', 'X')), ('X', ('X')), ('X', ('a')), ('X', (''))}, 
            'X')

    gramatica_a_testada = ({'X'}, 
            {'a', '+', '*'}, 
            {('X', ('X', '+', 'X')), ('X', ('X', '*', 'X')), ('X', ('X')), ('X', ('a'))}, 
            'X')

    gramatica_b = ({'E', 'F', 'V', 'T'}, 
                {'+', '*', 'a', 'b', 'c', '(', ')'}, 
                {('E', ('E', '+', 'T')), ('T', ('F')), ('T', ('T', '*', 'F')), ('E', ('')), ('T', ('')), ('E', ('T')),
                    ('F', ('V')), ('F', ('(', 'E', ')')), ('V', ('a')), ('V', ('b')), ('V', ('c'))}, 
                'E')

    gramatica_b_testada = ({'E', 'F', 'V', 'T'}, 
                {'+', '*', 'a', 'b', 'c', '(', ')'}, 
                {('E', ('T')), ('E', ('E', '+', 'T')), ('T', ('F')), ('T', ('T', '*', 'F')),
                    ('F', ('V')), ('F', ('(', 'E', ')')), ('V', ('a')), ('V', ('b')), ('V', ('c'))}, 
                'E')

    gramatica_c = ({'S'}, 
                {1, '+', 'a'}, 
                {('S', ('S', '+', 'S')), ('S', (1)), ('S', ('a')), ('S', (''))}, 
                'S')

    gramatica_c_testada = ({'S'}, 
                {1, '+', 'a'}, 
                {('S', ('S', '+', 'S')), ('S', (1)), ('S', ('a'))}, 
                'S')
    
    assert glc.remove_vazias(gramatica_a) == gramatica_a_testada
    assert glc.remove_vazias(gramatica_b) == gramatica_b_testada
    assert glc.remove_vazias(gramatica_c) == gramatica_c_testada
    
    