preço = float(input("Qual o valor da compra ? "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 3X no cartão
[ 4 ] 4X ou mais no cartão''')
opcao = int(input("Qual é a opção: "))

if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
elif opcao ==3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$ {:.2f}".format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra será parcela em {}X de R$ {:.2f} COM JUROS". format(totalparc, parcela))
else:
    total = preço
    print("OPÇÃO INVALIDA de pagamento. Tente novamente !")
print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final".format(preço, total))
