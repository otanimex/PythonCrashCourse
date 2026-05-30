#########################################################################
#   Python Crash Course                                                 #
#   Chapter 5 If Statements                                             #
#   Exercise 9 No users                                                 #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Add an if test to hello_admin.py (PythonCC_5_8.py) to make sure the #
#   list or users is not empty.                                         #
#       -   if the list is empty, print the message We need to find some#
#           users.                                                      #
#       -   Remove all of the usernames from your list, and make sure   #
#       -   the correct message is printed.                             #
#########################################################################

# user_names=["admin","gloria","manuel","jorge","tamara","gabriela"]
user_names=[]
name = "admin"

if len(user_names) == 0 and name == "admin":
    print("We need some users man")

if name in user_names:
    if name == "admin":
        print("Hello admin, remember sudo must not be used here \n")
    else:
        print("Hello "+name+" how are ya?")

for name in user_names:
    print("Remember to greet: "+name+"\n")

