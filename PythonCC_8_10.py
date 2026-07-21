#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 10 Great Magicians                                         #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Start with a copy of your program from Exercise 8-9. Write a func-  #
#   tion called make_great() that modifies the list of magicians by     #
#   adding the phrase Great to each magician's name. Call               #
#   show_magicians() to see that the list has actually been modified.   #
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

show_magicians(new_names)
