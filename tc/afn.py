'''
Autômato Finito Não Determinístico (AFN)
'''
# 2 - delta do AFN
def delta(automato, estado, simbolo):
    try:
        return automato[2][(estado, simbolo)]
    except KeyError:
        return {}


# o retorno é uma lista de estados
# passando referencia da lista ao inves de valor string. A diferença no AFN ocorre  quando ele esta entrando no estado (o que ainda nao é esse parte)

# 3 - Fecho-Epsilon
# A função eclose pode receber um estado com apenas um elemento (Set1 = 'a') ou um conjunto de elementos (Set2 = 'a','b','c','d').
def eclose(automato,estado):
    simbolo = ''   # O simbolo possui valor '' para definir como se fosse um épsilon.
    eclosure = set()   # Nesta linha foi criado um set vazio eclosure = { }
    for estados in estado:   # Este for serve para percorrer cada estado presente no Set de entrada(estado), seja eles Set1 ou Set2, por exemplo.
        eclosure = eclosure.union({estados}) # @Conrado Luiz Pela definição: q ∈ ECLOSE(q)
        eclosure = eclosure.union(delta(automato, estados, simbolo))  # Nesta linha o eclosure está utilizando o .union para somar o eclose de cada elemento do set de entrada e guardar na própria variável.
    return eclosure # Será retornado um Set com o resultado da soma do eclose de cada Set de entrada.

# 4 - Delta estendido do AFN
def delta_hat(automato, estado, palavra):
    if palavra == []:
        return estado
    else:
        simbolo = palavra.pop()
        fe = eclose(automato, estado)
        fn = set()
        for e in fe:
            estados = delta_hat(automato, {e}, palavra)
            deltas = [delta(automato, estado, simbolo) for estado in estados]
            fn = fn.union(*deltas)
        return fn
#Assim como no AFD a função vai partir do estado inicial recebido e recursivamente chamar a função delta() até o fim da palavra. Porém no AFN deverá calcular o fecho epsilon (fe)
#para cada estado e posteriormente chamar a função delta() para cada um dos estados preenchendo o vetor de estados encontrados (fn).


# 5 - Função aceitação
def aceita(automato, palavra): # palavra é um array com os simbolos. e.g. [1, 0, 1]
    estados_finais = delta_hat(automato, {automato[3]}, palavra)
    for estado in estados_finais:
        if estado in automato[4]:
            return True
    return False


# 6 - Computação do autômato
def computacao(automato, estado, palavra):
    if palavra == []:
        # Formatação para elementos finais do autômato
        return "(" + estado + ", )"
    else:
        # Subtrai o simbolo da palavra para uso futuro
        simbolo, palavra = a[0], a[1:]

        # Obtem a lista de estados partindo do atual
        estados = delta(automato, estado, simbolo)

        # Instancia o texto do primeiro estado
        texto_atual = "(" + estado + ", " + printw(palavra) + ") |- "

        # >> Parametros do loop
        # Mostra se é a primeira execução neste estado
        primeiro = True
        # Qtd de caracteres da linha anterior para formatar corretamente
        len_primeiro_texto = 0
        
        # Itera por todos estados possíveis a partir do Delta atual
        for proximo in estados:
            # Primeiro elemento deste estado
            if (primeiro):
                len_primeiro_texto = len(texto_atual)
                texto_atual = texto_atual + computacao(automato, proximo, palavra)
            # Elementos seguintes
            else:
                texto_atual = "\n" + (" " * len_primeiro_texto) + computacao(automato, proximo, palavra)
            primeiro = False

        return texto_atual
    
# 8 - Transformação AFN para AFD (simplificado)
def afn2afd_smart(automato):
  Sigma = automato[1] #Os autômatos devem reconhecer a mesma linguagem, logo o alfabeto é o mesmo para os dois
  QSet = set()
  Delta = dict()
  FSet = set()
  #Os estados, estados finais e transições ainda precisam ser computados, então os conjuntos são iniciados vazios
  estadoInicial = eclose(automato, automato[3]) #O estado inicial do autômato não-determinístico é passado como parâmetro para a função Fecho-Epsilon. O estado inicial do autômato determinístico será o mesmo do não-determinístico, ou todos os estados alcançados por transições vazias.
  QSet.union(estadoInicial)
  for estado in QSet:
    for simbolo in Sigma:
      proximoEstado = set()
      for elemento in estado: #A ordem dos for aninhados: Para cada estado, que pode ser 1 ou vários elementos, cada símbolo vai gerar 1 transição, para cada um dos elementos.
        proximoEstado.union(delta(automato, estado, simbolo))
        for pe in proximoEstado:
          proximoEstado.union(eclose(pe))
      if automato[4] in proximoEstado:
        FSet.union(proximoEstado)
      Delta[(estado, simbolo)]:proximoEstado
  automatoDeterministico = (QSet, Sigma, Delta, estadoInicial, FSet)
  return automatoDeterministico
