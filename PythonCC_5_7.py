#########################################################################
#   Python Crash Course                                                 #
#   Chapter 5 If Statements                                             #
#   Exercise 7 Favorite fruit                                           #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a list of your favorite fruits, and then write a series of     #
#   independent if statements that check for certain fruits in your     #
#   list.                                                               #
#########################################################################

favorite_fruits = ["Strawberry","Mangoes","Peaches"]

selected_fruit = "Mangoes"

if selected_fruit in favorite_fruits:
    print(selected_fruit + " is one of my favorites.")
else:
    print("Well that's not a favorite one.")
