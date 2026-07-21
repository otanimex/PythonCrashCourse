#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 11 Unchanged Magicians                                     #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Start with a copy of your program from Exercise 8-10. call the      #
#   function make_great() with a copy of the list of magician's names.  #
#   Because the original list will be unchanged, return the new list    #
#   Call show_magicians() with each listo to show that you have one     #
#   list of the original names and one list with the Great added to     #
#   each magician's name.                                               #
#########################################################################

def show_magicians(names):
    print("Eston son algunos de los grandes magos:")
    for name in names:
        print(name)
        
def make_great(names):
    new_list = []
    for name in names:
        new_name = "Great " + name
        new_list.append(new_name)
    return new_list


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

new_names = make_great(magicians_names)

show_magicians(magicians_names)

show_magicians(new_names)
