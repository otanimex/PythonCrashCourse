#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 5 Movie Tickets                                            #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   A movie theater charges different ticket prices depending on a      #
#   person's age. If a person is under the age of 3, the tickets is     #
#   free; if they are between 3 and 12 the ticket is $10; and if they   #
#   are over age 12, the ticket is $15. Write a loop which you ask      #
#   users their age, and then tell them the cost of their movie ticket. #
#########################################################################

loop = 0

while loop == 0:
    age = input("What's your age?")
    if int(age) <= 3:
        print("Your ticket is free!")
    elif int(age) > 3 and int(age) <= 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")


