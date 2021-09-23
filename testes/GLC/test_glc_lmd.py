import tc.glc as glc

# Implementação de testes da função lmd (tarefa 21)
# Aluna: Bruna Eduarda Rigueira Capistrano

def test_lmd():
    
    assert glc.lmd(({'X'}, 
                    {'a', '+', '*'}, 
                    {('X', ('X', '+', 'X')), ('X', ('X', '*', 'X')), ('X', ('X')), ('X', ('a'))}, 
                    'X'),
                   ['a', '+', 'a', '*', 'a']) == "X => X+X => a+X => a+X*X => a+a*X => a+a*a"
    
    assert glc.lmd(({'E', 'F', 'V', 'T'}, 
                    {'+', '*', 'a', 'b', 'c', '(', ')'}, 
                    {('E', ('T')), ('E', ('E', '+', 'T')), ('T', ('F')), ('T', ('T', '*', 'F')),
                     ('F', ('V')), ('F', ('(', 'E', ')')), ('V', ('a')), ('V', ('b')), ('V', ('c'))}, 
                    'E'),
                    ['a', '*', 'b', '+', '(', 'c', '+', '(', 'a', '+', 'c', ')', ')']) == "E => E+T => T+T => T*F+T => F*F+T => V*F+T => a*F+T => a*V+T => a*b+T => a*b+F => a*b+(E) => a*b+(E+T) => a*b+(T+T) => a*b+(F+T) => a*b+(V+T) => a*b+(c+T) => a*b+(c+F) => a*b+(c+(E)) => a*b+(c+(E+T)) => a*b+(c+(T+T)) => a*b+(c+(F+T)) => a*b+(c+(a+T)) => a*b+(c+(a+F)) => a*b+(c+(a+V)) => a*b+(c+(a+c))"
    
    assert glc.lmd(({'S'}, 
                    {1, '+', 'a'}, 
                    {('S', ('S', '+', 'S')), ('S', (1)), ('S', ('a'))}, 
                    'S'), 
                   [1, '+', 1, '+', 'a']) == "S => S+S => 1+S => 1+S+S => 1+1+S => 1+1+a"
    
    assert glc.lmd(({'E'}, 
                    {'a', 'b', '+', '-'}, 
                    {('E', ('E', '+', 'E')), ('E', ('E', '-', 'E')), ('E', ('a')), ('E', ('b'))}, 
                    'E'), 
                   ['a', '-', 'b', '+', 'a']) == "E => E+E => E-E+E => a-E+E => a-b+E => a-b+a"
    
    assert glc.lmd(({'A', 'B', 'S'}, 
                    {'a', 'b', ''}, 
                    {('S', ('A', 'B')), ('S', ('')), ('A', ('a', 'B')), ('B', ('S', 'b'))}, 
                    'S'), 
                   ['a', 'b', 'b']) == "S => AB => aBB => aSbB => abB => abSb => abb"
    
    assert glc.lmd(({'A', 'B', 'S'}, 
                    {'a', 'b'}, 
                    {('S', ('a', 'B')), ('S', ('b', 'A')), ('S', ('a', 'S')), ('S', ('b', 'A', 'A')), 
                     ('S', ('a')), ('S', ('b')), ('S', ('b', 'S')), ('S', ('a', 'B', 'B'))}, 
                    'S'), 
                   ['a', 'a','b', 'b', 'a', 'b', 'b', 'a']) == "S => aB => aaBB => aabB => aabbS => aabbaB => aabbabS => aabbabbA => aabbabba"
    
    assert glc.lmd(({'A', 'B', 'S'}, 
                    {0, 1, ''}, 
                    {('S', ('A', 1, 'B')), ('A', (0, 'A')), ('A', ('')), ('B', (0, 'B')), 
                     ('B', (1, 'B')), ('B', (''))}, 
                    'S'), 
                   [0, 0, 1, 0, 1]) == "S => A1B => 0A1B => 00A1B => 001B => 0010B => 00101B => 00101"
    
    assert glc.lmd(({'S', 'T'}, 
                    {'a', 'b', ''}, 
                    {('S', ('T', 'b', 'T')), ('T', ('a', 'T', 'b')), ('T', ('b', 'T', 'a')), ('T', ('T', 'T')), 
                     ('T', (''))}, 
                    'S'), 
                   ['a', 'b', 'b', 'a', 'b', 'a', 'b']) == "S => TbT => aTbbT => abbT => abbaTb => abbabTab => abbabab"
    
    assert glc.lmd(({'S', '(', ')'}, 
                    {'(', ')', ''}, 
                    {('S', ('(', 'S', ')')), ('S', ('S', 'S')), ('S', (''))}, 
                    'S'), 
                   ['(', '(', ')', '(', ')', ')']) == "S => (S) => (SS) => ((S)S) => (()S) => (()(S)) => (()())"
    
    assert glc.lmd(({'S', 'A', 'B'}, 
                    {'a', 'b', 'c', ''}, 
                    {('S', ('A', 'B')), ('A', ('')), ('A', ('a', 'A')), ('B', ('b', 'B', 'c')), ('B', (''))}, 
                    'S'), 
                   ['a', 'b', 'b', 'c', 'c']) == "S => AB => aAB => aB => abBc => abbBcc => abbcc"
    
    
    assert glc.lmd(({'S', 'A'}, 
                    {'a', 'b', '&'}, 
                    {('S', ('S', '&', 'S')), ('S', ('A')), ('A', ('a')), ('A', ('b'))}, 
                    'S'), 
                   ['a', '&', 'b']) == "S => S&S => A&S => a&S => a&A => a&b"