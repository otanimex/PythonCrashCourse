#########################################################################
#   Python Crash Course                                                 #
#   Chapter 6 Dictionaries                                              #
#   Exercise 11 Cities                                                  #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Make a dictionary called cities. Use the names of three cities      #
#   as keys in your dictionary. Create4 a dictionary of information     #
#   about each city and include the country that the city is in,        #
#   its approximate population, and one fact about that city. The       #
#   keys for each city's dictionary shoul be something like country,    #
#   population, and fact. Print the name of each city and all of the    #
#   information you hava stored about it.                               #
#########################################################################

cities = {"Londres":{"country":"England",
              "population":"9.1M",
              "fact":"Here's the big ben"},
          "Paris":{"country":"France",
              "population":"66.7M",
              "fact":"Here's the Eiffel tower"},
          "Rome":{"country":"Italy",
              "population":"2.7M",
              "fact":"Zero calcare lives in Rome"},
          }

for city, data in cities.items():
    print("-----------------------------------\nCity: " + city + "\n" +
          "País: " + data['country'] + "\n" +
          "Población: " + data['population'] + "\n" +
          "Dato: " + data['fact'] + "\n" 
          )
