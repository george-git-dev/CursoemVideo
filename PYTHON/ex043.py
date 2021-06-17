altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)
#imc = peso / (altura ** 2)


print("SEU IMC É: {:.2f}".format(imc))

if imc <= 18.5:
    print("Abaixo do Peso")
elif imc >= 18.6 and imc <= 25.0:
    print("Peso Ideal")
elif imc >= 25.1 and imc <= 30.0:
    print("Sobrepeso")
elif imc >= 30.1 and imc <= 40.0:
    print("Obesidade")
else:
    print("Obesidade Mórbida")