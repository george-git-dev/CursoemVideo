times = ("Fortaleza", "Athletico-PR", "Atlético-MG", "Bragantino", "Palmeiras",
         "Bahia", "Flamengo", "Atlético-GO", "Fluminense", "Santos", "Corinthians", "Ceará",
         "Internacional", "Cuiabá", "São Paulo", "Chapecoense", "Juventude", "Sport", "América-MG", "Grêmio")

print("-=" * 15)
print(f"Lista de times: {times}")
print("-=" * 15)
print(f"Os 5 primeiros são {times[0:5]}")
print(f"Os 4 últimos são {times[-4:]}")
print(f"Times em ordem alfabética {sorted(times)}")
print(f"O Chapecoense está na {times.index('Chapecoense')+1}ª posição")


