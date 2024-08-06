#1 - Lista de palavras
#2 - Selecionar uma palavra aleatoria
#3- Dividir cada letra e transformar em espaços
#4 - Sistema de adivinhação
#5 - Sistema de loop de perda e acerto
import random
        
palavras = ['cachorro', 'pessoa', 'computador', 'escola', 'borracha', 'bola']
print("Bem vindo ao Jogo da Forca!!!")
print('Deseja jogar?')
escolha = input("Sua escolha: ")
if escolha != "0":
    palavra = random.choice(palavras)
    palavra_forca = [letra for letra in palavra]
    print("************************************")
    print("Sua palavra escolhida foi: \n")
    palavra_vazia = []
    for letra in palavra_forca:
        palavra_vazia.append("_")
    print(*palavra_vazia, sep=" ")
    print("\nO jogo se inicia, boa sorte!")
    print("************************************")

    tentativas = 0

    while palavra_vazia != palavra_forca and tentativas < 5:
        print(f"***************{tentativas}/5*TENTATIVAS*****************")
        tentativa = input("Digite uma letra: ")
        if tentativa in palavra_forca:
            for index, letra in enumerate(palavra_forca):
                if letra == tentativa:
                    palavra_vazia[index] = tentativa
            print(f"Você acertou uma letra! A letra {tentativa} existe na palavra!")
        else:
            print("Você errou! Tente novamente")
            tentativas+=1
        print(' '.join(palavra_vazia))

    if palavra_vazia == palavra_forca:
        print("************************************")
        print("Parabéns, você ganhou!")
    else:
        print("************************************")
        print("Você perdeu! A palavra era:", ''.join(palavra_forca))
    
    
    
