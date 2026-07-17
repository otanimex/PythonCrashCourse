#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 5 Cities                                                    #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function called describe_city() that accepts the name of    #
#   a city and its country. The function should print a simple sente-   #
#   nce, such as Reyjavik is in Iceland. Give the parameter for the     #
#   country a default value. Call your function for three cities, at    #
#   least one of wich is not in the default country.                    #
#########################################################################

def describe_city(city, country="México"):
    print("The city " + city + " is located in " + country + ".")
    
cities = {"Paris":"France",
          "Mazatlan":"",
          "Culiacan":"",
          "Monterrey":"",
          "Rome":"Italy"}

for city, country in cities.items():
    if country == "":
        country = "México"
    describe_city(city, country)
