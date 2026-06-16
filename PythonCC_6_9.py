#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 9 Favorite Places                                          #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a dictionary called favorite_places. Think of three names      #
#   to use as keys in the dictionary, and store one to three favorite   #
#   places for each person. To make this exercise a bit more interesting#
#   , ask some friends to name a few of their favorite places. Loop     #
#   through the dictionary, and print each person's name and their      #
#   favorite places.                                                    #
#########################################################################

favorite_places = {"Hercules":{"Primer":"Thebas",
                       "Segundo":"Athenas",
                       "Tercero":"Spartha"
                       },
                   "Megara":{"Primer":"Athenas",
                       "Segundo":"Vesubio",
                       "Tercero":"Corinto"
                       },
                   "Zeus":{"Primer":"Olympus",
                       "Segundo":"Athenas",
                       "Tercero":"Rhodas"
                       },
                   "Ades":{"Primer":"Ades",
                       "Segundo":"Elyseum Gardens",
                       "Tercero":"Olympus"
                       }
                   }

for name, place in favorite_places.items():
    print("Los lugares favoritos de " + name + " son: \n 1." + 
          place['Primer'] + "\n 2." +
          place['Segundo'] + "\n 3." + 
          place['Tercero'] + "\n" +
          "-----------------------------------"
          )
