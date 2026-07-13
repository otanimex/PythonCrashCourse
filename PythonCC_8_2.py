#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 2 Favorite Book                                            #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function called favorite_book() htat accepts one parameter, #
#   title. The function should print a message, such as One of my       #
#   favorite books is Alice in Wonderland. Call the function, making    #
#   sure to include a book title as an argument in the funcion call.    #
#########################################################################

def favorite_book(title):
    print("One of my favorite books is:" + title)

book = input("Write the title of your favorite book: ")

favorite_book(book)
