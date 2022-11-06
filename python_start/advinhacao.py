print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 42

num_user = input("Digite o seu numero: ")

print("Você digitou o número ", num_user_str)

num_user = int(num_user_str)

if(numero_secreto == num_user):
    print("Você acertou!")
else:
    print("Você errou!")