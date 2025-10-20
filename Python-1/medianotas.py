nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
print('Tirando {} e {} a média do aluno é {}'.format(nota1, nota2, media))
if 7 > media >=5:
    print('O aluno está de recuperação')
elif media < 5:
    print('O aluno está reprovado!')
elif media >= 7:
    print('O aluno está aprovado')
