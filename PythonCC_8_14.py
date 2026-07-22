#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 14 Cars                                                    #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function that stores information about a car in a dictionary#
#   The funtion should always receive a manufacturer and a model name.  #
#   It should then accept an arbitrary number of keyword arguments.     #
#   Call the function with the requiered information and two other      #
#   name-value pairs, such as a color or an optional feature. Your      #
#   function should work for a call like this one:                      #
#   ----------------------------------------------------------------    #
#   car = make_car('subaru', 'outback', color='blue' tow_package=True   #
#   ----------------------------------------------------------------    #
#   Print the dictionary that's returned to make sure all the infor-    #
#   mation was stored correctly.                                        #
#########################################################################

def make_car(manufacturer,model, **characteristhics):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in characteristhics.items():
        car[key] = value
    return car

beat = make_car('Chevrolet','Beat',year=2018,version='Hatchback')

print(beat)
