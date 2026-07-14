#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 3 T-Shirt                                                  #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function called make_shirt() that accepts a size and the    #
#   text of a message that should be printed on the shirt. The function #
#   should print a sentence summarizing the size of the shirt and the   #
#   message printed on it. Call the function once using positional      #
#   argumentas to make a chirt. Call the function a second time using   #
#   keyword arguments.                                                  #
#########################################################################

def make_shirt(size="XL", text="No trans, no live"):
    print("Shirt size: " + size + "\nText: " + text)

make_shirt("L","I reject my mortal flesh")

make_shirt()
