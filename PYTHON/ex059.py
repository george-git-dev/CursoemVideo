from time import sleep
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
opcao = 0
while opcao != 5:
    print('''Por favor insira uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input("Digite: "))
    if opcao == 1:
        soma = n1 + n2
        print("O resultado da soma de {} e {} é {}".format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print("O resultado da multiplicação de {} e {} é {}".format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior é {}".format(n1, n2, maior))
    elif opcao == 4:
        print("Informe os números novamente:")
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
    elif opcao == 5:
        print("Finalizando:")
    else:
        print("Opção inválida. Tente novamente")
    print("=-=" * 10)
    sleep(2)
print("Fim do programa")

