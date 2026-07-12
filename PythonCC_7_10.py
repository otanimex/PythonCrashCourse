#########################################################################
#   Python Crash Course                                                 #
#   Chapter 7 User input and while loops                                #
#   Exercise 10 Dream Vacation                                          #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a program that polls users about their dream vacation. Write  #
#   a prompt similar to If you could visit one place in the world,      #
#   where would you go? Include a block of code that prints the result  #
#   of the poll.                                                        #
#########################################################################

poll = {}
loop = True
while loop == True:
    name = input("What's your name?")
    if name == 'quit':
        break
    place = input("Where would you go to your dream vacation?")
    poll[name] = place

for names, places in poll.items():
    print(name + " would like to go to: " + place)


