preco = float(input('Preço da compra: R$'))
print('''Forma de pagamento 
      [1] a vista dinheiro/cheque
      [2] a vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra sera parcelada em {}x de R${:.2f} com juros '.format(totalparcela, parcela))
print('Sua compra vai custar {:.2f}'.format(total))