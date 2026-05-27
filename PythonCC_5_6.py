#########################################################################
#   Python Crash Course                                                 #
#   Chapter 5 If Statements                                             #
#   Exercise 6 Stages of life                                           #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write an if-elif-else chain that determinesa person's stage of life #
#   Set the value for the age for the variable age and then:            #
#       -   If the person is less than 2 years old, print a message that#
#           the person is a baby.                                       #
#       -   If the person is at least 2 years old but less than 4, print#
#           a message that the person is a toddler.                     #
#       -   If the person is at least 4 years old but less than 13,     #
#           print a message that the person is a kid.                   #
#       -   If the person is at least 13 years old but less than 20,    #
#           print a message that the person is a teenager.              #
#       -   If the person is at least 20 years old but less than 65,    #
#           print a message that the person is an adult.                # 
#       -   If the person is at least 65 or older,print a message that  #
#           that the person is an elder.                                #
#########################################################################

#The variable must have a range between 0 and 100
age = 31
#I should put some variable verification

#The stage of life printer
if (age < 2):
    print("Eres un bebe, ni has de poder leer esto")
elif (age >= 2 or age < 13):
    print("Eres un infante")
elif (age >= 13 or age < 20):
    print("Eres un niño")
elif (age >= 20 or age < 65):
    print("Eres un adulto, ¿comó va la rodilla?")
elif (age >= 65):
    print("Eres viejo")
else:
    print("¿Pues que tan grande eres?")
