import os
os.system

lista_numeros = []
par = 0
impar = 0

for i in range(6):
    numeros = int(input(f"digite o {i+1}ª número: "))
    lista_numeros.append(numeros) 
    if numeros %2 == 0:
        par += 1
    else:
        impar +=1


print(f"a quantidade de números par é de {par}")
print(f"a quantidade de números impares é de {impar}")
    
