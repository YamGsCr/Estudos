import random
import baralho
import logging

# Configurar o logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

suit = baralho.suit
valor = baralho.valor

def blackjack_inicio():
    jogador_pontos = baralho.puxarDuasCartas(suit, valor)
    dealer_pontos = baralho.puxarCarta(suit, valor)
    return jogador_pontos, dealer_pontos

def blackjack_stand(jogador, dealer):
    dealer_revelar = baralho.puxarCarta(suit, valor)
    dealer += dealer_revelar
    logging.debug(f"Dealer revela: {dealer_revelar}, total do dealer: {dealer}")

    if dealer < 13:
        dealer += baralho.puxarCarta(suit, valor)
        logging.debug(f"Dealer tem menos de 8, puxa mais uma carta, total do dealer: {dealer}")

        if dealer < jogador:
            dealer += baralho.puxarCarta(suit, valor)
            logging.debug(f"Dealer tem menos que o jogador, puxa mais uma carta, total do dealer: {dealer}")

            if dealer > 21:
                logging.debug("Dealer estourou!")
                return jogador, dealer
            elif dealer < jogador:
                dealer += baralho.puxarCarta(suit, valor)
                logging.debug(f"Dealer tem menos que o jogador novamente, puxa mais uma carta, total do dealer: {dealer}")

                if dealer > 21:
                    logging.debug("Dealer estourou!")
                    return jogador, dealer
                elif dealer > jogador:
                    logging.debug("Dealer tem mais que o jogador!")
                    return jogador, dealer
                else:
                    logging.debug("Dealer tem o mesmo que o jogador!")
                    return jogador, dealer
        elif dealer > jogador:
            logging.debug("Dealer tem mais que o jogador!")
            return jogador, dealer
    elif dealer > jogador:
        logging.debug("Dealer tem mais que o jogador!")
        return jogador, dealer

    logging.debug("Fim da jogada do dealer.")
    return jogador, dealer

def blackjack_hit(jogador,dealer):
    jogador_hit = baralho.puxarCarta(suit, valor)
    logging.debug(f"O jogador dá hit e puxar uma carta de {jogador_hit} pontos")
    jogador+= jogador_hit
    if jogador > 21:
        logging.debug("O jogador estourou!")
        return jogador, dealer
    else:
        dealer_revelar = baralho.puxarCarta(suit, valor)
        dealer += dealer_revelar
        logging.debug(f"Dealer revela: {dealer_revelar}, total do dealer: {dealer}")

        if dealer < 13:
            dealer += baralho.puxarCarta(suit, valor)
            logging.debug(f"Dealer tem menos de 8, puxa mais uma carta, total do dealer: {dealer}")

            if dealer < jogador:
                dealer += baralho.puxarCarta(suit, valor)
                logging.debug(f"Dealer tem menos que o jogador, puxa mais uma carta, total do dealer: {dealer}")

                if dealer > 21:
                    logging.debug("Dealer estourou!")
                    return jogador, dealer
                elif dealer < jogador:
                    dealer += baralho.puxarCarta(suit, valor)
                    logging.debug(f"Dealer tem menos que o jogador novamente, puxa mais uma carta, total do dealer: {dealer}")

                    if dealer > 21:
                        logging.debug("Dealer estourou!")
                        return jogador, dealer
                    elif dealer > jogador:
                        logging.debug("Dealer tem mais que o jogador!")
                        return jogador, dealer
                    else:
                        logging.debug("Dealer tem o mesmo que o jogador!")
                        return jogador, dealer
            elif dealer > jogador:
                logging.debug("Dealer tem mais que o jogador!")
                return jogador, dealer
        elif dealer > jogador:
            logging.debug("Dealer tem mais que o jogador!")
            return jogador, dealer

        logging.debug("Fim da jogada do dealer.")
        return jogador, dealer
 