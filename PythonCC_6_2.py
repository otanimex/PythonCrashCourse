#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 2 Favorite Numbers                                         #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Use a distionary to store people's favorite numbers. Think of five  #
#   names, and use them as keys in your dictionary. Think of a favorite #
#   number for each person, and store each as a value in your dictionary#
#   Print each person's name and their favorite number. For even more   #
#   fun, poll a few friends and get some actual data for your program.  #
#########################################################################

listadoNumeros = {"Margarita":1,
                  "Mordecai":1,
                  "Rigby":8,
                  "Eileen":4,
                  "Papaleta":91,
                  "Benson":7}

print(listadoNumeros)

for persona, numero in listadoNumeros.items():
    print(persona + ": " + str(numero))
