#

import os 
os.system("cls")

lista_notas = []

for i in range(4):
    nota = int(input(f"informe a sua {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum (lista_notas)
media = soma / 4

if lista_notas[i] >=7:
    resultado = "aprovado"
elif lista_notas[i] >= 5:
    resultado= "recuperação"
else:
    resultado = "reprovado"
print(f"Media:{media}")
print(f"resultado: {resultado}")

