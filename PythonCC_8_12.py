#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 12 Sandwiches                                              #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function that accepts a list of items a perso wants on a    #
#   sandwich. The function should have one parameter that collects as   #
#   many items as the function call provides, and it should print a     #
#   summary of the sandwich that is being ordered. Call the function    #
#   three times, using a different number of arguments each time.       #
#########################################################################

def sandwich(ingridients):
    n = 1
    for ingridient in ingridients:
        print(str(n) + ". " + ingridient)
        n += 1

print("Type the ingridients you want in your sandwich: ")

sandwich_ingridients = []

while True:
    ing = input("Escribe el ingrediente, si deseas salir escribe 1: ")
    if ing == str(1):
        break
    sandwich_ingridients.append(ing)
    

sandwich(sandwich_ingridients)

