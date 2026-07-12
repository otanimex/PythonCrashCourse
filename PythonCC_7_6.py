#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 3 Three exits                                              #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write different versions of either Excercise 7-4 or 7-5 that do     #
#   each of the following at least once:                                #
#   -   Use a conditional test in the while statement to stop the loop. #
#   -   Use an active variable to control how long the loop runs.       #
#   -   Use a break statement to exit the loop when the user enters a   #
#       'quit' value.                                                   #
#########################################################################

#Inicia 7.4

print("The program will write the toppings you want when all ended type quit")

toppings=[]
loop = True #Changed to be a conditional an logical
while loop == True:
    topping = input("What topping do you want to add to your pizza?\n")

    if topping == "quit": #already contained
        print("The toppings in your pizza will be:\n")
        for top in toppings:
            print(" -   " + top)
        break
    else:
        toppings.append(topping)

# Inicia 7.5

loop = 0

while loop <= 10: #active variable
    age = input("What's your age?")
    if int(age) <= 3:
        print("Your ticket is free!")
    elif int(age) > 3 and int(age) <= 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
    loop += 1


