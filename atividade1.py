#crie um programa que solicite do úsuario 3 notas, armazenando em um vetor e calcule a media aritimetica

import os
os.system

lista_notas = []

for i in range(3):
    nota = int(input(f"digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma / 3

print(f"a media final foi de {media}: ")

