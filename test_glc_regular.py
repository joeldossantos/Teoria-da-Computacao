from tc import glc

assert glc.regular(({'S', '(', ')'},
                    {'(', ')', ''},
                    {('S', ('(', 'S', ')')), ('S', ('S', 'S')), ('S', (''))},
                    'S')) == ("Gramatica não Regular")

# print(glc.regular(({'S', '(', ')'},
#                     {'(', ')', ''},
#                     {('S', ('(', 'S', ')')), ('S', ('S', 'S')), ('S', (''))},
#                     'S')))


# 
# 
# 
# 

assert glc.regular( 
    (
        {'S'},
        {0,1},
        {
            ('S', ('')),
            ('S', (0)),
            ('S', (1)),
            ('S', (0,'S',0)),
            ('S', (1,'S',1))
        },
        'S'
    )) == ("Gramatica não Regular")


# print(glc.regular( 
#     (
#         {'S'},
#         {0,1},
#         {
#             ('S', ('')),
#             ('S', (0)),
#             ('S', (1)),
#             ('S', (0,'S',0)),
#             ('S', (1,'S',1))
#         },
#         'S'
#     )))


# 
# 
#
# 

assert glc.regular( 
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
    )) == ("Gramática Linear à Direita")

# print(glc.regular( 
#     (
#         {'S', 'A'},
#         {'a','b'},
#         {
#             ('S', ('a','S')),
#             ('S', ('b','S')),
#             ('S', ('A')),
#             ('A', ('a','a')),
#             ('A', ('b','b'))
#         },
#         'S'
#     )))


#
#
#
#


assert glc.regular( 
    (
        {'S', 'A'},
        {'a','b'},
        {
            ('S', ('A','a','a')),
            ('S', ('A','b','b')),
            ('A', ('A','a')),
            ('A', ('A','b')),
            ('A', (''))
        },
        'S'
    )) == ("Gramática Linear à Esquerda")


# print(glc.regular( 
#     (
#         {'S', 'A'},
#         {'a','b'},
#         {
#             ('S', ('A','a','a')),
#             ('S', ('A','b','b')),
#             ('A', ('A','a')),
#             ('A', ('A','b')),
#             ('A', (''))
#         },
#         'S'
#     )))