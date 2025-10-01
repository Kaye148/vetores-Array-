import os
os.system("cls")

#criando um vertor (lista de nota)
lista_notas = []

for i in range (3):
    nota = int(input(f"digite a {i+1}ª nota : "))
    lista_notas.append(nota)

soma = sum(lista_notas)

#print(f"Nota: {lista_notas} ")
#print(f"Nota: {lista_notas[2]} ")

for i in range(3):
    print(f"Nota: {lista_notas[i]}")

print(f"Soma: {soma}")

#print(f"Soma {soma}")
print("FIM")
