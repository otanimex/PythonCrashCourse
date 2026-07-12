#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 9 No Pastrami                                              #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Using the list sandwich_orders from Exercise 7-8, make sure the     #
#   sandwich 'pstrami? appears in the list at least three times. Add    #
#   code near the beginning of your program to print a message saying   #
#   the deli run put of pastrami, and then use awhile loop to remove    #
#   all occurrences of 'pastrami' from sandwich_orders. Make sure no    #
#   pastrami sandwiches end up in finished_sandwiches.                  #
#########################################################################

sandwich_orders = ["Tuna",
                   "Pizza",
                   "Meatball",
                   "Pastrami",
                   "Parmesian Chicken",
                   "Ham & cheese",
                   "Pastrami",
                   "Porkbelly",
                   "BBQ",
                   "Pastrami"]

while "Pastrami" in sandwich_orders:
    print("Thereś no more Pastrami")
    sandwich_orders.remove("Pastrami")

finished_sandwiches = []

for order in sandwich_orders:
    print("Your " + order + " it's ready.")
    finished_sandwiches.append(order)
    #sandwich_orders.remove(order)
print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
