import tc.er as er



#implementação
#aluno: Vinicius Tavares dos Santos Nunes

#expressão regular: 1*(11+00)

r = er.er2afn_base(1)
s = er.er2afn_base(0)


a = er.er2afn_concat(r, r)
b = er.er2afn_concat(s, s)
c = er.er2afn_union(a, b)
d = er.er2afn_kleene(r)

#er.er2afn('*', 1,[+,1100])
