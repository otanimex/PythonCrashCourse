#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 8 Pets                                                     #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make several dictionaries, where the name of each dictionary is the #
#   name of a pet. In each dictionary, include the kind of animal and   #
#   the owner's name. Store these dictionaries in a list called pets.   #
#   Next, loop through your list and as you do print everything you     #
#   know about each pet.
#########################################################################

Scooby  = {"Name":"Scooby",
      "Species":"Dog",
      "Owner":"Shaggy"
        }

Rufus   = {"Name":"Rufus",
      "Species":"Naked Mole Rat",
      "Owner":"Ron"
        }

Arroz   = {"Name":"Arroz",
      "Species":"Cat",
      "Owner":"Ren"
        }

Spirit  = {"Name":"Spirit",
      "Species":"Horse",
      "Owner":"Fortuna"
        }

Daifuku = {"Name":"Daifuku",
      "Species":"Bunny",
      "Owner":"Satoru"
        }

pets = [Scooby, Rufus, Arroz, Spirit, Daifuku]

for pet in pets:
    print( "--------------------------------------------------------\n" +
           "Nombre: " + pet['Name'].title() + "\n" +
           "Especie: " + pet['Species'].title() + "\n" +
           "Dueño: " + pet['Owner'].title()
          )
