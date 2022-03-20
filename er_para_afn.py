import tc.er as er
import os


#implementação
#aluno: Vinicius Tavares dos Santos Nunes

#expressão regular: 1*(11+00)

def teste_operadores():

    r = er.er2afn_base(1)
    s = er.er2afn_base(0)
    print("base: ",r,s)


    a = er.er2afn_concat(r, r)
    b = er.er2afn_concat(s, s)
    print("concatenação: ", a,b)
    c = er.er2afn_union(a, b)
    print("união", c)
    d = er.er2afn_kleene(r)
    print("fecho kleene: ", d)

def teste_er2af():

    a = er.er2afn(('*', '1'))
    b = er.er2afn(('', '1', '1'))
    c = er.er2afn(('', '0', '0'))
    d = er.er2afn(('+', 'b', 'c'))
    e = er.er2afn(('', 'd', 'e'))
    print('fecho kleene:', a)
    print('concatenação:', b)
    print('concatenação:', c)
    print('união: ', d)
    print('concatenação final: ', e)
    
os.system('python -m pytest testes -vv')
