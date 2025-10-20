from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Precisa se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Vc deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))