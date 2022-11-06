print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 42

num_user_str = input("Digite o seu numero: ")

print("Você digitou o número ", num_user_str, end="\n\n")

num_user = int(num_user_str)

if(numero_secreto == num_user):
    print("Você acertou!")
else:
    if(num_user > numero_secreto):
        print("Seu chute foi maior que o número secreto")
    elif(num_user < numero_secreto):
        print("Seu chute foi menor que o número secreto")
    print("Você errou!")

print("Fim de Jogo!!!")