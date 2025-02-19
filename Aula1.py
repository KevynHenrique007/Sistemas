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