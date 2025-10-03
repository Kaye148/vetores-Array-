import os 
os.system("cls")

numeros = []

for i in range(5):
    numero = int(input(f"digite um número {i+1}ª :"))
    if numero < 0:
        numero = 0
    numeros.append(numero)

for i, numero in enumerate (numeros, start=1):
    print(f"{i}º número  {numero} ")

