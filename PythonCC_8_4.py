#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 4 Large Shirts                                             #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Modify the make_shirt() funtion so that shirts are large by         #
#   default with a message that reads I love Python. Make a large       #
#   shirt and a medium shirt with the default message, and a shirt      #
#   of any size with a different message.                               #
#########################################################################

def make_shirt(size="L", text="Trans love the python"):
    print("Shirt size: " + size + "\nText: " + text)

make_shirt("L")

make_shirt("M")

make_shirt(text="Holy trans")
