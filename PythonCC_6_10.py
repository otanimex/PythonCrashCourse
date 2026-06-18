#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 10 Favorite Numbers                                        #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Modify your program from Exercise  6-2 (page 102) so each person    #
#   can have more than one favorite number. Then print each person's    #
#   name along with their favorite numbers.                             #
#########################################################################

listadoNumeros = {"Margarita":{'most':1,'almost':2,'last':3},
                  "Mordecai":{'most':10,'almost':20,'last':30},
                  "Rigby":{'most':4,'almost':3,'last':7},
                  "Eileen":{'most':5,'almost':4,'last':9},
                  "Papaleta":{'most':91,'almost':73,'last':210},
                  "Benson":{'most':7,'almost':9,'last':13}}

print(listadoNumeros)

for persona, numero in listadoNumeros.items():
    print(persona + ": " + str(numero['most']) + ", " +
          str(numero['almost']) + ", " + str(numero['last']))
