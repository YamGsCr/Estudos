import baralho
import blackjack
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
suit = baralho.suit
valor = baralho.valor

print("Bem vindo ao Cassino Às de Diamante!")
print("O que deseja jogar?")
print("1 - Blackjack")
print("0 - Mostrar quantia de dinheiro")
dinheiro = float(100)
escolha = int(input("Sua escolha: "))
while dinheiro > 10:
  if 0:
    print(f"Você tem R${dinheiro}")
  elif 1:
    print("Você vai jogar blackjack, quanto irá apostar?")
    aposta_inicial = float(input("Sua aposta: "))
    print("Vamos iniciar o jogo!")
    print("--------------------------------------------------")
    jogador, dealer = blackjack.blackjack_inicio()
    print("--------------------------------------------------")
    print(f"Pontuação inicial - Jogador: {jogador}, Dealer: {dealer}")
    jogada = input("Qual será sua próxima jogada? (stand, hit ou double?): ")
    jogada = jogada.lower()
    if jogada == "stand":
      print("Você decidiu: STAND")
      print("-------------------")
      jogador, dealer = blackjack.blackjack_stand(jogador, dealer)
      print("-------------------")
      print(f"Pontuação final - Jogador: {jogador}, Dealer: {dealer}")
      if dealer > 21:
        print("VOCÊ VENCEU!")
        print(f"Resultado da aposta: {aposta_inicial*1.5}")
        dinheiro+=(aposta_inicial*1.5)
      elif jogador < dealer or jogador == dealer:
        print("VOCÊ PERDEU!")
        dinheiro-=aposta_inicial
      else:
        print("VOCÊ VENCEU!")
        print(f"Resultado da aposta: {aposta_inicial*1.5}")
        dinheiro+=(aposta_inicial*1.5)
    elif jogada == "hit":
      print("Você decidiu: HIT")
      print("-------------------")
      jogador, dealer = blackjack.blackjack_hit(jogador, dealer)
      print("-------------------")
      print(f"Pontuação final - Jogador: {jogador}, Dealer: {dealer}")
      if jogador > 21:
        print("VOCÊ PERDEU!")
        dinheiro-=aposta_inicial
      elif dealer > 21:
        print("VOCÊ VENCEU!")
        print(f"Resultado da aposta: {float(aposta_inicial)*1.5}")
        dinheiro+=(float(aposta_inicial)*1.5)
      elif jogador < dealer or jogador == dealer:
        print("VOCÊ PERDEU!")
        dinheiro-=aposta_inicial
      else:
        print("VOCÊ VENCEU!")
        print(f"Resultado da aposta: {float(aposta_inicial)*1.5}")
        dinheiro+=(float(aposta_inicial)*1.5)
    elif jogada == "double":
      aposta_double = float(aposta_inicial)*2
      print("Você decidiu: DOUBLE")
      print(f"Você dobrou sua aposta: {aposta_double}")
      print("-------------------")
      jogador, dealer = blackjack.blackjack_hit(jogador, dealer)
      print("-------------------")
      print(f"Pontuação final - Jogador: {jogador}, Dealer: {dealer}")
      if jogador > 21:
        print("VOCÊ PERDEU!")
        dinheiro-=aposta_double
      elif dealer > 21:
        print("VOCÊ VENCEU!")
        print(f"Resultado da aposta: {float(aposta_double)*1.5}")
        dinheiro+=(float(aposta_double)*1.5)
      elif jogador < dealer or jogador == dealer:
        print("VOCÊ PERDEU!")
        dinheiro-=aposta_double
      else:
        print("VOCÊ VENCEU!")
        print(f"Resultado da aposta: {float(aposta_double)*1.5}")
        dinheiro+=(float(aposta_double)*1.5)
      
    
