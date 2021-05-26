def delta(mt, estado, simbolo):
    try:
        prox_estado, novo_simbolo, direcao = mt[3][(estado,simbolo)]
        return prox_estado, novo_simbolo, direcao
    except:
        return(None,None,None)


# 58 - Computação da MT
# Claudio Freitas
def computacao(mt, palavra):
  transicoes = mt[3]
  estado_simboloFita = []
  estado_simboloFita_direcao = []
  direcao = ''
  for key in transicoes:
    for prv in palavra:
      estado_simboloFita = key
      estado_simboloFita_direcao = transicoes[key]
      if estado_simboloFita_direcao[2] == 'R': 
        direcao = 'direita.'
      else: 
        direcao = 'esquerda.'
      if estado_simboloFita_direcao[0] == estado_simboloFita[0] and estado_simboloFita[1] == prv: 
        print('Troca o estado ', estado_simboloFita_direcao[0], ' para a variável ', estado_simboloFita_direcao[1], ' ao ler o valor ', prv, ' e segue para a ', direcao)
      elif estado_simboloFita_direcao[0] != estado_simboloFita[0] and estado_simboloFita[1] == prv:
        print('Troca o estado ', estado_simboloFita_direcao[0], ' para a variável ' , estado_simboloFita_direcao[1]
            , ', segue para o estado ', estado_simboloFita_direcao[0],' ao ler o valor ', prv, ' e segue para a ', direcao)
      else:
        print('Leitura atual não muda por aceitar valor ', estado_simboloFita[1], '. Palavra no valor ', prv)