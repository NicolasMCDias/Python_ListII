#jogo de adivinhacão:
from random import randint
cop = randint(1,5) #Faz "pensar"
p = int(input("Tente adivinha o valor escolhido de 1 à 5: "))
if p == cop:
    print("VOCÊ ACERTOU, O VALOR ERA {} !!".format(p))
else:
    print("Você errou !! o valor escolhido era: {}".format(cop))