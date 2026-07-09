#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 3 Multiples of ten                                         #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Ask the user for a number, and then report whether the number is    #
#   a multiple of 10 or not.                                            #
#########################################################################

number = input("What's the number you're checking if it's multiple of 10?\n")
print("Let me see if the number " + number + " is multiple of 10.")

modulo = int(number) % 10

if modulo > 0:
    print("Looks like the number " + number + " is not a number 10 multiple")
else:
    print("Looks like the number " + number + " is a number 10 multiple")



