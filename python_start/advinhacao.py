print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    num_user_str = input("Digite o seu numero: ")
    print("Você digitou o número ", num_user_str)

    num_user = int(num_user_str)
    acertou = numero_secreto == num_user
    maior = num_user > numero_secreto
    menor = num_user < numero_secreto

    if acertou :
        print("Parabéns, você acertou!")
    else:
        if(maior):
            print("Seu chute foi maior que o número secreto")
        elif(menor):
            print("Seu chute foi menor que o número secreto")
        print("Você errou!", end="\n\n")
    rodada = rodada + 1

print("Fim de Jogo!!!")