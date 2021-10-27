import tc.er as er

#implementação linha 8
#aluno: Igor Feital Lopes

#expressão regular: 0*(1+0)*

exp = ('',('*',0),('*',('+',1,0)))

expected_afn = ({'i4', 'i1', 'f5', 'f1', 'f2', 'f3', 'i5', 'i2', 'f4', 'i3'}, {0, 1}, {('i4', ''): {'f4', 'i1'}, ('f1', ''): {'f3'}, ('i1', 0): {'f1'}, ('f4', ''): {'i5'}, ('i5', ''): {'f5', 'i3'}, ('f3', ''): {'f5', 'i3'}, ('i3', ''): {'i2', 'i1'}, ('f2', ''): {'f3'}, ('i2', 1): {'f2'}}, 'i4', {'f5'})

expected_er2afn = ({'i6', 'f10', 'i9', 'f11', 'i7', 'f7', 'i10', 'i8', 'i11', 'f8', 'f6', 'f9'}, {0, 1}, {('i7', ''): {'f7', 'i6'}, ('f6', ''): {'f7', 'i6'}, ('i6', 0): {'f6'}, ('f7', ''): {'i11'}, ('i11', ''): {'i10', 'f11'}, ('f10', ''): {'i10', 'f11'}, ('i10', ''): {'i8', 'i9'}, ('f8', ''): {'f10'}, ('f9', ''): {'f10'}, ('i8', 1): {'f8'}, ('i9', 0): {'f9'}}, 'i7', {'f11'})

def create_afn():
  #base
  base0 = er.er2afn_base(0)
  base1 = er.er2afn_base(1)

  #union
  union = er.er2afn_union(base1,base0)

  #kleene
  r = er.er2afn_kleene(base0)
  s = er.er2afn_kleene(union)

  #concat
  afn = er.er2afn_concat(r,s)

  return afn

def test_er2af():
  assert create_afn() == expected_afn
  assert er.er2afn(exp) == expected_er2afn