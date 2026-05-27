#########################################################################
#   Python Crash Course                                                 #
#   Chapter 5 If Statements                                             #
#   Exercise 8 Hello Admin                                              #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a list of five or more usernames, including the name 'admin'.  #
#   Imagine you are writing code that will print a greeting to each user#
#   after they log in to a website. Loop through the list, and print a  #
#   greeting to each user:                                              #
#       -   If the username is 'admin', print a special greeting, such  #
#           as Hello admin would you like to see a status report?       #
#       -   Otherwise, print a generic greeting, such as Hello Eric,    #
#           thank you for logging in again.                             #
#########################################################################

user_names=["admin","gloria","manuel","jorge","tamara","gabriela"]

name = "gloria"

if name in user_names:
    if name == "admin":
        print("Hello admin, remember sudo must not be used here \n")
    else:
        print("Hello "+name+" how are ya?")

for name in user_names:
    print("Remember to greet: "+name+"\n")

