import random

sorteio = random.randint(1,10)
print("###  JOGO DA ADIVINHAÇÃO")
print("Adivinhe o número que estou pensando, de 1 a 10")
chute = int(input("digite seu chute:"))
print(sorteio)
print(chute)

if (chute == sorteio):
    print("Parabéns, você acertou o número! o número era ", sorteio)
if (chute !=sorteio):
    print("Você errou! O número era", sorteio)

limite_tentativas = 3
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
    elif (chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("Chute um número menor!")
    tentativa = tentativa + 1 
