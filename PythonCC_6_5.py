#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 5 Rivers                                                   #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a dictionary containing three major rivers and the country each#
#   river runs through. One key-value pair might be 'nile':'egypt'.     #
#   -   Use a loop to print a sentence about each river, such as The    #
#       Nil runs through Egypt.                                         #
#   -   Use a loop to print the name of each river included in the       #
#       dictionary.                                                     #
#   -   Use a loop to print the name of each country included in the    #
#       dictionary.
#########################################################################

rivers = {'Amazon':'Brazil',
          'Yangtze':'China',
          'Mississippi':'USA',
          'Yenisey':'Russia',
          'Rio de la plata':'Argentina'}

for river, country in rivers.items():
    print('The '+river+' river runs through '+country+'.')

for river in rivers.keys():
    print(river)

for river in rivers:
    print(rivers[river])
