#########################################################################
#   Python Crash Course                                                 #
#   Chapter 5 If Statements                                             #
#   Exercise 10 Checking Usernames                                      #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Do the following to create a program that simulates how websites    #
#   ensures that everyone has a unique username:                        #
#       -   Make a list of five or more usernames called                #
#           current_users.                                              #
#       -   Make another list of five usernames called new_users list   #
#           Make sure one or two of the new usernames are also in the   #
#           current_users list.                                         #
#       -   Loop trough the new_users list to see ir each new username  #
#           has already been used. If it has, print a message that the  #
#           person will need to enter a new username. If a username has #
#           not been used, print a message saying that username is      #
#           available.                                                  #
#       -   Make sure your comparison is case sensitive. If 'John' has  #
#           been used, 'JOHN' should not be accepted.                   #
#########################################################################

current_users=["John","Juan","Pablo","Gaby","Hector","Maria",
               "Daniela","Jorge","Noemi","Jessy"]

new_users=["Angel","DANIELA","Jorge","Jessy","Maria","Carlos","Jill",
           "Leilani","Frida","Secco","Pauline","Sahra","Zero","Josefina",
           "Moira","Claire"]

for user in current_users:
    for newuser in new_users:
        if newuser.upper() == user.upper():
            print ("Ya existe, sorry cambiale")
            break
    print("The username is available cool")


