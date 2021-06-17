from datetime import date

anoAtual = date.today().year
anoNascimento = int(input("Digite seu ano de nascimento: "))

idade = anoAtual - anoNascimento

print("Quem nasceu em {} tem {} anos em {}". format(anoNascimento, idade, anoAtual))

if idade == 18:
    print("Você tem que se alistar imediatamente !")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento".format(saldo))
    ano = anoAtual + saldo
    print("Seu alistamento será em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você ja deveria ter se alistado há {} anos" .format(saldo))
    ano = anoAtual - saldo
    print("Seu alistamento foi em {}".format(ano))

