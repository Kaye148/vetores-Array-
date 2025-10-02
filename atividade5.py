import os 
os.system

menu = []
pratos = []
precos = []

while True:
    print("""
código \t prato \t valor  
    1   \t Picanha \t 25.00
    2   \t  Lasanha \t 20.00
    3   \t  Strogonoff \t 18.00
    4   \t  Bife Acebolado \t 15.00
    5   \t  Pão com ovo \t 5.00  
""")
       
    
    menu = int(input("digite o còdigo referente ao prato: "))
    mais_pedidos = input("deseja fazer um novo pedido?\nUse S ou N para responder: ").upper



    match menu:

        case 1:
            pratos.append("Picanha")
            precos.append(25)
            print("se deseja continuar com o pedido aprte o "" ")
        case 2:
            pratos.append("Lasanha")
            precos.append(20)
        case 3:
            pratos.append("Strogonoff")
            precos.append(18)
        case 4:
            pratos.append("Bife Acebolado")
            precos.append(15)
        case 5:
            pratos.append("Pão com Ovo")
            precos.append(5)
        case _:
            print("opção invalida.")
            print("tente novamente...")
            preco = 0

            preco_total = preco_total + preco

            mais_pedidos = input("deseja fazer um novo pedido?\nUse S ou N para responder: ").upper

            if mais_pedidos =="N":
                break



print(f"total a pagar: {preco_total}")

 