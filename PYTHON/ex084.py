temp = []
principal = []
maior = 0
menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar ? [S/N] "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Ao todo, você cadastrou {len(principal)}")
print(f"O maior peso foi de {maior} kg ", end="")
for p in principal:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor} kg. Peseo de ", end="")
for p in principal:
    if p [1] == menor:
        print(f"[{p[0]}] ", end="")
print()