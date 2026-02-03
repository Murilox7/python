from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:
    print('''
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}:'.format(v1, v2, soma))
    elif opcao == 2:
        produto = v1 * v2
        print('o resultadode de {} x {} é {}'.format(v1, v2, produto))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')