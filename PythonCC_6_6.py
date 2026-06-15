#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 6 Polling                                                  #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Use the code in favorite_languages.py                               #
#   -   Make a list of people who should take the favorite languages    #
#       poll. Include some names that are already in the dictionary and #
#       some that are not.                                              #
#   -   Loop through the list of people who should take the poll.       #
#       If they have already taken the poll, print a message thanking   #
#       them for responding. If they have not yet taken the poll, print #
#       a message inviting them to take the poll.                       #
#########################################################################

#Code inside the book:

favorite_languages = {
        'jen':'ṕython',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languge is " + 
          language.title() + ".")

#code of resolution
poll = ['puttin','selensky','trump','edward','phil','jen']

for name in poll:
    if name in favorite_languages:
        print(" Thank you " + name.title() + " for doing the poll.")
    else:
        print(" Please " + name.title() + " do the poll.")


