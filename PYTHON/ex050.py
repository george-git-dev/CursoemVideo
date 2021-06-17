'''
s = 0
for c in range(0, 6):
    n = int(input("Digite um número: "))
    resultado = n % 2
    if resultado == 0:
        s += n
print("O somatório de todos os valores foi {}".format(s))
'''

# ou

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite o {} valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} números pares e a soma foi {}".format(cont, soma))
