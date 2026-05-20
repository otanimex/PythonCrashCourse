#Aunque ya no puedo comer pizza aquí van mis favoritas:
pizzas=["La de casa","Carnes frias","Hawaiana","Mexicana","Pastor"]
mensajePizzas="A mi realmente me gusta la pizza de: "
pizzasAmigos=pizzas[:]
pizzas.append("Ranchera")
pizzasAmigos.append("Anchoas")
print("Mis Pizzas")
for pizza in pizzas:
    print(mensajePizzas+pizza)
print("Realmente extraño la pizza")
print("Las Pizzas de mis amigos")
for pizza in pizzasAmigos:
    print(mensajePizzas+pizza)
print("No se que les gusta realmente")

