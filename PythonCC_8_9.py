#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 9 MAgicians                                                #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a list of magician's names. Pass the list to a function ca-    #
#   lled show_magicians(), which prints the name of each magician in    #
#   the list.                                                           #
#########################################################################

def show_magicians(names):
    print("Eston son algunos de los grandes magos:")
    for name in names:
        print(name)
        
magicians_names = ["Houdini",
                   "Criss Angel",
                   "Barney Stinson",
                   "Dai Vernon",
                   "Paul Daniels",
                   "Juan Tamariz",
                   "David Copperfield",
                   "Lance Burton",
                   "David Blaine",
                   "Justin William",
                   "Dynamo"]

show_magicians(magicians_names)
