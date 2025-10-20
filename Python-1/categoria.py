#Confederação Nacional de natação: leia o ano de nascimento e mostre sua categoria
from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
if idade <= 9:
    print('Sua categoria é mirim!')
elif idade <= 14:
    print('Sua categoria é infantil!')
elif idade <= 19:
    print('Sua categoria é junior!')
elif idade <= 25:
    print('Sua categoria é sênior!')
else:
    print('Sua categoria é master!')