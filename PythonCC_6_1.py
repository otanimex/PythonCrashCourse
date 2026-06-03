#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 1 Person                                                   #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Use a dictionary to store information about a person you know. Store#
#   their first name, last name, age, and the city in wich they live.   #
#   You should have keys such as first_name, last_name, age and city.   #
#   Print each piece of information stored in your dictionary.          #
#########################################################################

someone = {'first_name':'Alguien',
           'last_name':'Peréz',
           'age':45,
           'city':'Tamagandapio'}

print('Conozco a una persona llamada ' + someone['first_name'] + ' ' + 
      someone['last_name'] + ' que tiene ' + str(someone['age']) + 
      ' años de edad y vive en ' + someone['city'] +'.')

