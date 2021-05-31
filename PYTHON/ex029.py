velocidade = float(input("Qual é a velocidade atual do carro ? "))
if velocidade > 80:
    print("Multado !")
    multa = (velocidade-80) * 7
    print("Você deve pagar uma multa de RS{:.2f}!".format(multa))
print("Tenha um Bom dia")