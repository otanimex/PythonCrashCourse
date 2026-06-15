#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 7 People                                                   #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Start with the program you wrote for Exercise 6-1. Make two new     #
#   dictionaries representing different people, and store all three     #
#   dictionaries in a list called people. Loop through your list of     #
#   people. As you loop through the list, print everything you know     #
#   about each person.                                                  #
#########################################################################

someone0 = {'first_name':'Alguien',
           'last_name':'Peréz',
           'age':45,
           'city':'Tamagandapio'}

someone1 = {'first_name':'Fulano',
           'last_name':'Rodríguez',
           'age':56,
           'city':'Salamanca'}

someone2 = {'first_name':'Mengano',
           'last_name':'Quintana',
           'age':67,
           'city':'USME'}

people=[someone0, someone1, someone2]

for person in people:

    print('Conozco a una persona llamada ' + person['first_name'] + ' ' + 
      person['last_name'] + ' que tiene ' + str(person['age']) + 
      ' años de edad y vive en ' + person['city'] +'.')

