#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 6 City Names                                               #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function called city_country() that accepts the name of     #
#   a city and its country. The function should return a string for-    #
#   matted like this:                                                   #
#   "Santiago, Chile"                                                   #
#   Call your function with at least three city-country pairs, and      #
#   print the value that's returned.                                    #
#########################################################################

def city_country(city, country="Mexico"):
    return(city + ", " + country)
    
cities = {"Paris":"France",
          "Mazatlan":"",
          "Culiacan":"",
          "Monterrey":"",
          "Rome":"Italy"}

for city, country in cities.items():
    if country == "":
        country = "Mexico"
    print(city_country(city, country))
