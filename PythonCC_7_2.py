#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 2 Restaurant Seating                                       #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a program that asks ht euser how many people are in their     #
#   dinner group. If the answer ir more than eigth, print a message     #
#   saying they'll have to wait for a table. Otherwise, report that     #
#   their table is ready.                                               #
#########################################################################

seats = input("How many people are we expecting?\n")
print("Let me see if I can find you a " + seats +" table.")
if int(seats) >= 8:
    print("Sorry there's no tables, you'll have to wait")
else:
    print("Your table is ready, please come with me")



