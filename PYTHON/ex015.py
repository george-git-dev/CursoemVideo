# Aluguel de carros

dias = int(input("Quantos dias alugados ? "))
km = float(input("Quantos Km rodados ? "))
pago = (dias * 60) + (km * 0.15)
print("O toal a pagar é de R$ {:.2f}".format(pago))
