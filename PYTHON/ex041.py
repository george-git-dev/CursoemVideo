from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))

idade = atual - nascimento

if idade <= 9:
    print("MIRIM")
elif idade >= 10 and idade <= 14:
    print("INFANTIL")
elif idade >= 15 and idade <= 19:
    print("JÚNIOR")
elif idade >= 20 and idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")

