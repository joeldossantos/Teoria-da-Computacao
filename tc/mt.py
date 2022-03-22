import re

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

# 59 - Computação da MT que pode permanecer parada
# Bernardo Simoes do Nascimento
def computacaoComParada(mt, palavra):
  estados = mt[0]
  simbolosAlfabeto = mt[1]
  simobolosFita = mt[2]
  estadoInicial = mt[4]
  branco = mt[5]
  estadoFinal = mt[6]
  letras = ''
  for letra in simbolosAlfabeto:
    letras = letras + letra
  regex = '^[{}]*'.format(letras) 
  formato = re.compile(regex) 

  if re.fullmatch(formato, palavra):
    print('String valida')
  else:
    print('A string deve conter apenas os simbolos: ' + letras)
    return 'String invalida'

  lst = []
  for i in palavra:
      lst.append(i)
  cabecaLeitura = 0
  proxEstado = estadoInicial
  contador = 0
  while True: 
    simbolo = lst[cabecaLeitura]
    estadoAtual = proxEstado 
    
    print('Estado atual: ', estadoAtual)
    print('Simbolo atual: ', simbolo)
    proxEstado, novoSimbolo, direcao = delta(mt, proxEstado, simbolo)
    contador = contador + 1
    if (proxEstado == None and estadoAtual not in estadoFinal):
      print('Palavra nao aceita')
      print(estadoAtual)
      aceito = False
      break
    if (proxEstado == None and estadoAtual in estadoFinal):
      print('Palavra aceita')
      print(estadoAtual)
      aceito = True
      break

    txt = ('Indo do estado {} para o estado {}, trocando o simbolo {} por {}').format(estadoAtual, proxEstado, lst[cabecaLeitura], novoSimbolo)

    print(txt)
    lst[cabecaLeitura] = novoSimbolo
    

    if direcao == 'R':
      cabecaLeitura = cabecaLeitura + 1
      print('Movimentando a cabeça de leitura para direita')
    elif direcao == 'L':
      if(cabecaLeitura == 0):
        lst = [branco] + lst
      else:
        cabecaLeitura = cabecaLeitura - 1
      print('Movimentando a cabeça de leitura para esquerda')
    elif direcao == 'S':
      cabecaLeitura = cabecaLeitura
      print('Mantendo a cabeça de leitura parada')

    if(cabecaLeitura > len(lst)-1):
      lst.append(branco)
    print('Cabeca leitura', cabecaLeitura)
    print('Fita: ', lst)

  palavraFinal = ''
  if(aceito):
    for l in lst:
      if l != branco:
        palavraFinal = palavraFinal + l

  print('Posicao cabecaLeitura: ', cabecaLeitura)
  print('Nº de movimentos: ', contador)
    #print('Palavra Final ', palavraFinal) 

  return palavraFinal, aceito



def move_fila(fila, ponteiro, direcao, branco='B'):
  new_fila = fila
  new_ponteiro = ponteiro

  if direcao == 'L':
    new_ponteiro = ponteiro - 1
    if new_ponteiro < 0:
      new_ponteiro = 0
      new_fila = [branco, *fila]
    
  if direcao == 'R':
    new_ponteiro = ponteiro + 1
    if new_ponteiro >= len(fila):
      new_fila = [*fila, branco]
    
  return new_fila, new_ponteiro

def movimento(mt, palavra):
  fila = [*palavra]
  estado_atual = mt[4]
  estados_finais = mt[-1]
  ponteiro = 0
  branco = mt[5]

  while estado_atual not in estados_finais:
    result = delta(mt, estado_atual, fila[ponteiro])
    estado_atual, new_symbol, direcao = result

    fila[ponteiro] = new_symbol
    fila, ponteiro = move_fila(fila, ponteiro, direcao)

  return fila