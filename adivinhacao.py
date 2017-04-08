import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)	#Cria o numero secreto com a função randrange que vai de 0 a 100.
    total_de_tentativas = 0
    pontos = 1000
    nivel = 0

# Valida entrada de nível
    while not 1 <= nivel <= 3:
        try:
            print("Qual nível de dificuldade?")
            print("(1)Fácil\n(2)Médio\n(3)Difícil")
            nivel = int(input("Defina o nível: "))
        except ValueError:
            print("Por favor, insira um número!")
		
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        try:
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute = int(input("Digite um número entre 1 e 100: "))
        except ValueError:
            print("Digite somente números!")
        else:
            print("Você digitou " , chute)
            
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()