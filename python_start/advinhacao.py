print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 42

num_user_str = input("Digite o seu numero: ")

print("Você digitou o número ", num_user_str, end="\n\n")

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
    print("Você errou!")

print("Fim de Jogo!!!")