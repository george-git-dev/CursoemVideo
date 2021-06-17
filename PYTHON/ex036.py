valorCasa = float(input("Qual o valor da casa ? "))
salario = float(input("Qual é o salário ? "))
prazo = int(input("Qual é o prazo em anos ? "))

prestacao = valorCasa / (prazo * 12)
limite = salario * 30 / 100

print("Para pagar uma casa de R$ {:.3f} em {} anos a prestação será de R$ {:.3f}". format(valorCasa, prazo, prestacao))

if prestacao <= limite:
    print("Seu emprestimo foi aprovado ! ")
else:
    print("Seu emprestimo não foi aprovado !")
