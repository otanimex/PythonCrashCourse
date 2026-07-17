#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 8 User Album                                               #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Start with your program from Exercise 8-7. Write a while loop that  #
#   allows users to enter an album's artist and title. Once you have    #
#   that information, call make_album() with the user's input and print #
#   the dictionary that's created. Be sure to include a quit value      #
#   in the while loop.                                                  #
#########################################################################

def make_album(artist, title, tracks=''):
    album = {'artist':artist,'title':title}
    if tracks:
        album['tracks'] = tracks
    return album

underMySkin=make_album('Avril Lavigne', "Under My Skin", 13)
conspiracyOfOne=make_album('Offspring', 'Conspiracy of One', 14)
allOrNothing=make_album('Pennywise', 'All or Nothing', 12)

print(underMySkin)
print(conspiracyOfOne)
print(allOrNothing)

while True:
    print("Este programa toma nombres de albumes y sus datos")
    album = input("Escribe el nombre del album: ")
    artista = input("Escribe el nombre del artista: ")
    canciones = input("Escribe la cantidad de caciones en el album: ")

    print(make_album(album, artista, canciones))

    salida = input('Si deseas salir aprieta 1 ')
    if salida == "1":
        break
