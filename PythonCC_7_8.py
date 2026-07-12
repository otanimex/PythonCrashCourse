#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 8 Deli                                                     #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a list called sandwich_orders and fill it with the names of    #
#   various sandwiches. Then make an empt list called                   #
#   finished_sandwiches. Loop through the list of sandwiches and print  #
#   a message for each order, such as I made your tuna sandwich. As     #
#   each sandwich is made, move it to the lis of finished sandwiches.   #
#   After all the sandwiches have been made, print a message listing    #
#   each sandwich that was made.                                        #
#########################################################################

sandwich_orders = ["Tuna",
                   "Pizza",
                   "Meatball",
                   "Parmesian Chicken",
                   "Ham & cheese",
                   "Porkbelly",
                   "BBQ"]

finished_sandwiches = []

for order in sandwich_orders:
    print("Your " + order + " it's ready.")
    finished_sandwiches.append(order)
    #sandwich_orders.remove(order)
print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
