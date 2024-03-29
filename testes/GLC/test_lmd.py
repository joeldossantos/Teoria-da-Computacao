from tc import glc

# Function to test glc.lmd()
# Student : Adeoye Sunday Ladele


def test_lmd():
    assert glc.lmd(({'S'}, {0, 1}, {('S', ()), ('S', (0)), ('S', (1)),
                                    ('S', (0, 'S', 0)), ('S', (1, 'S', 1))}, 'S'),
                   [1, 0, 0, 1]) == "S => 1S1 => 10S01 => 1001"
    assert glc.lmd(({'S', 'A', 'B'}, {'a', 'b'}, {('S', ('a', 'B')),
                                                  ('S', ('b', 'A')), ('A', ('a', 'a', 'A')), (
        'B', ('b', 'b', 'B')), ('A', ('S')), ('B', ('S')), ('A', ()), ('B', ())}, 'S'),
        ['b', 'a', 'a', 'a', 'b', 'b']) == "S => bA => baaB =>  baaS => baaaB => baaabb"
    assert glc.lmd(({'S', 'C'}, {0, 1}, {('S', (0, 1, 'S')), ('S', (1, 0, 'S')),
                   ('S', ('C')), ('C', (1, 1, 1))}, 'S'), [0, 1, 1, 1, 1]) == "S => 01S => 01C => 01111"
    assert glc.lmd(({'E', 'I'}, {'+', '*', '(', ')', 'a', 'b', 0, 1},
                   {('E', ('I')), ('E', ('E', '+', 'E')), ('E', ('E', '*', 'E')), ('E', ('(', 'E', ')')),
                   ('I', ('a')), ('I', ('b')), ('I', ('I', 'a')), ('I', ('I', 'b')), ('I', (0)), ('I', (1)), ('I', ())}, 'E'),
                   ['(', 'a', '+', 'b', ')', '+', '1']) == "E => E+E => (E)+E => (E+E)+E => (I+E)+E => (a+E)+E => (a+I)+E => (a+b)+E => (a+b)+I => (a+b)+1"
    assert glc.lmd(({'S', 'A'}, {'a', 'b'}, {('S', ('A', 'A', 'a')), ('S', ('A', 'A', 'b')),
                                             ('A', ('A', 'a')), ('A', ('A', 'b')), ('A', (''))}, 'S'),
                   ['b', 'b', 'a']) == "S => AAa => AbAa => AbbAa => bbAa => bba"
    assert glc.lmd(({'S', 'T'}, {'x', 'y', '+', '-', '/'}, {('S', ('S', '+', 'T')), ('S', ('S', '-', 'T')), ('S',
                   ('S', '/', 'T',)), ('S', ('T')), ('T', ('x')), ('T', ('y')), ('T', ('x', 'y'))}, 'S'),
                   ['x', 'y', '+', 'y', '-', 'x']) == "S => S-T => S+T-T => T+T-T => xy+T-T => xy+y-T => xy+y-x"
    assert glc.lmd(({'S', }, {'a', 'b'}, {('S', ('a', 'S', 'b', 'S')), ('S',
                   ('b', 'S', 'a', 'S'), ('S', ()))}, 'S'), ['a', 'a', 'b', 'b']) == "S => aSbS => aaSbSbS => aabSbS => aabbS => aabb"
    assert glc.lmd(({'S', 'T'}, {'(', ')', 'a', 'b'}, {('S', ('(', 'T', ')')), ('T', ('a',
                   'a', 'T')), ('T', ('b', 'b', 'T')), ('T', ())}, 'S'),
                   ['(', 'a', 'a', 'b', 'b', ')']) == "S => (T) => (aaT) => (aabbT) => (aabb)"
    assert glc.lmd(({'S', 'Q'}, {'(', '+', '-'}, {('S', ('(', 'S')), ('S', ('Q')),
                   ('Q', ('+', 'Q')), ('Q', ('-', 'Q')), ('Q', ())}, 'S'),
                   ['(', '(', '+', '-']) == "S => (S => ((S =>((Q => ((+Q => ((+-Q => ((+-"
    assert glc.lmd(({'S,', 'T'}, {1, 0}, {('S', (1, 1, 'S')), ('S', ('T')), ('T',
                   (0, 0, 'T')), ('T', ('S')), ('S', ()), ('T', ())}, 'S'),
                   [1, 1, 0, 0, 1, 1]) == "S => 11S => 11T => 1100T => 1100S => 110011S => 110011"
