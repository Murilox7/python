from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 1 e 10')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador >= 10:
        print('Escreva somente de 1 a 10! ')
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez') 
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('Acertou com {} palpites'.format(palpites))
      