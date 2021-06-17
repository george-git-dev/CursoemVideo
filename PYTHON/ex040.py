nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(media)

if media >= 7.0:
    print("Aluno aprovado !")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em recuperação")
else:
    print("aluno reprovado")

