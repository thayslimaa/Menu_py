print("*********MENU-PIZZAS******** ")
print("1 - Pizza Grande............ R$49,00")
print("2 - Pizza Média......... ..R$37,00")
print("3 - Pizza Pequena...... R$20,00")


op = input("Escolha o tamanho da pizza: ")
match op:
    case "1":
        print("Pizza grande")
        quntpg = int(input("Quantas pizzas grande você deseja? "))
        valor_pizza = quntpg * 49
        print("O valor é igual a R$", valor_pizza, ",00")
    case "2":
        print("Pizza média")
        quntpm = int(input("Quantas pizzas média você deseja? "))
        valor_pizza = quntpm * 37
        print("O valor é igual a R$", valor_pizza, ",00")
    case "3":
        print("Pizza pequena")
        quntpp = int(input("Quantas pizzas pequena você deseja? "))
        valor_pizza = quntpp * 20
        print("O valor é igual a R$", valor_pizza, ",00")

print("******MENU-BEBIDAS******")
print("1 - Coca-cola2L........ R$13,00")
print("2 - cola-cola1L..... R$7,00")
print("3 - Marácuja..... R$6,00")
print("4 - Laranja..... R$4,00")
print("5 - Não desejo bebida")


bebida = int(input("Escolha sua bebida "))
match bebida:
    case 1:
        print("Coca-cola2L")
        quntcc = int(input("Quantos refrigerantes? "))
        valor_bebida = quntcc * 13
        print("O valor é igual a R$", valor_bebida, ",00")
    case 2:
        print("cola-cola1L")
        quntcl = int(input("Quantos refrigerantes? "))
        valor_bebida = quntcl * 7
        print("O valor é igual a R$", valor_bebida, ",00")
    case 3:
        print("Marácuja")
        quntMJ = int(input("Quantos sucos? "))
        valor_bebida = quntMJ * 6
        print("O valor é igual a R$", valor_bebida, ",00")
    case 4:
        print("Suco de Laranja")
        quntl = int(input("Quantos sucos? "))
        valor_bebida = quntl * 4
        print("O valor é igual a R$", valor_bebida, ",00")
   


t = valor_pizza + valor_bebida
print("O valor total do pedido da pizza com as bebidas é R$", t) 
