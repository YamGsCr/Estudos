import random
suit = ["♣" , "♦" , "♥" , "♠"]
valor = ["2","3","4","5","6","7","8","9","10","J", "Q", "K", "A"]
def puxarCarta(suit, valor):
  suit_random = random.randint(0,len(suit)-1)
  valor_random = random.randint(0,len(valor)-1)
  suit = suit[suit_random]
  valor = valor[valor_random]
  carta = f'''
  ___________________
  |                 |
  | {suit}               |
  |                 |
  |                 |
  |                 |
  |                 |
  |        {valor}        |
  |                 |
  |                 |
  |                 |
  |               {suit} |
  |                 |
  |_________________|
  '''
  print(carta)
  if (valor == "J") or (valor == "Q") or (valor == "K"):
    valor = 10
  if (valor == "A"):
    valor = 1
  return int(valor)

def puxarDuasCartas(suit,valor):
  suit2 = suit
  valor2 = valor
  suit_random = random.randint(0,len(suit)-1)
  valor_random = random.randint(0,len(valor)-1)
  suit = suit[suit_random]
  valor = valor[valor_random]
  suit_random2 = random.randint(0,len(suit)-1)
  valor_random2 = random.randint(0,len(valor)-1)
  suit2 = suit2[suit_random2]
  valor2 = valor2[valor_random2]
  carta = f'''
  ___________________
  |                 |
  | {suit}               |
  |                 |
  |                 |
  |                 |
  |                 |
  |        {valor}        |
  |                 |
  |                 |
  |                 |
  |               {suit} |
  |                 |
  |_________________|
  '''
  carta2 = f'''
  ___________________
  |                 |
  | {suit2}               |
  |                 |
  |                 |
  |                 |
  |                 |
  |        {valor2}        |
  |                 |
  |                 |
  |                 |
  |               {suit2} |
  |                 |
  |_________________|
  '''
  print(carta)
  print(carta2)
  variaveis = ["J", "Q", "K"]
  if (valor == "J") or (valor == "Q") or (valor == "K"):
    valor = 10
  if (valor == "A") or (valor2 == "A"):
    if (valor == variaveis) or (valor2 == variaveis):
      valor = 11
    else:
      valor = 1
  return int(valor)+int(valor2)
