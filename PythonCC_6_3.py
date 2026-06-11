#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 3 Glossary                                                 #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   A Python dictionary can be used to model an actual dictionary.      #
#   However, to avoid confusion, let's call ia a glossary.              #
#   -   Think of five programming words you've learned about in the     #
#       previous chapters. Use thesewords as the keys in your glossary  #
#       and store their meanings as values.                             #
#   -   Print each word and its meaning as neatly formatted output. You #
#       might print the word followed by a colon and then its meaning   #
#       or print the word on one line and then print its meaning        #
#       indented on a second line. Use the newline character (\n) to    #
#       insert a blank lines between each word-meaning pair in your     #
#       output.                                                         #
#########################################################################

glossary = {"string":"A type of data that stores letters and characters",
            "integer":"A type of data that stores numbers without point",
            "list":"A list of one kind of data type values",
            "variable":"The name of a particular data value",
            "loop":"A control structure that repeat a part od the code"}

for word, definition in glossary.items():
    print(word + ": \n      " + definition) 
