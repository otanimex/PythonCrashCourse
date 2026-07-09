#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 4 Pizza Toppings                                           #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a loop that prompts the user to enter a series of pizza       #
#   toppings until they enter a 'quit' value. As they enter each        #
#   topping, print a message saying you'll add that topping to their    #
#   pizza.                                                              #
#########################################################################


print("The program will write the toppings you want when all ended type quit")

toppings=[]
loop = 0
while loop == 0:
    topping = input("What topping do you want to add to your pizza?\n")

    if topping == "quit":
        print("The toppings in your pizza will be:\n")
        for top in toppings:
            print(" -   " + top)
        loop = 1
    else:
        toppings.append(topping)



