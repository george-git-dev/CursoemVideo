# Reajuste salarial

salario = float(input("Qual é o salário do funcionário ? R$ "))
novo = salario + (salario * 15 / 100)

print("Um funcionário qye ganhava R$ {:.2f}, com 15% de aumento, passsa a receber R$ {:.2f}".format(salario, novo))
