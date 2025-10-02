import os 
os.system

numeros = []
soma_positivo = 0
quantidade_negativo = 0

for i in range(4):
        numero = int(input(f"digite o {i+1}ª número: "))
        numeros.append(numero)
        if numero >0:
                soma_positivo +=1
        else:
                quantidade_negativo +=1

soma = numero + soma_positivo


print(f"a soma dos números é de {soma}")
print(f"print o número que você digitou é um numero negativo {quantidade_negativo}")


                
       

       
    