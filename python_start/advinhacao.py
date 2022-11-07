print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 42
total_tentativas = 3

for rodada in range (1, total_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    num_user_str = input("Digite um numero entre 1 e 100: ")
    print("Você digitou o número ", num_user_str)
    num_user = int(num_user_str)

    if(num_user < 1 or num_user > 100):
        print("Você deve digitar um número entre 1 e 100!!!", end="\n\n")
        continue

    acertou = numero_secreto == num_user
    maior = num_user > numero_secreto
    menor = num_user < numero_secreto

    if acertou :
        print("Parabéns, você acertou!")
        break
    else:
        if(maior):
            print("Seu chute foi maior que o número secreto")
        elif(menor):
            print("Seu chute foi menor que o número secreto")
        print("Você errou!", end="\n\n")

print("Fim de Jogo!!!")