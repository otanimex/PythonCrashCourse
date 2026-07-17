#########################################################################
#   Python Crash Course                                                 #
#   Chapter 8 Functions                                                 #
#   Exercise 7 Album                                                    #
#   By Otanimex                                                         #
#   Instructions:                                                       #
#   Write a function called make_album() that builds a dictionary       #
#   describing a music album. The function should take in an artist     #
#   name and a album title, and it should return a dictionary contai-   #
#   ning these two pices of information. Use the function to make       #
#   three dictionaries representing different albums. Print each re-    #
#   turn value to show that the dictionaries are storing the album      #
#   information correctly.                                              #
#   Add an optional parameter to make_album() that allows you to store  #
#   the number of tracks on an album. If the calling line includes a    #
#   value for the number of tracks, add that value to the album's dic-  #
#   tionary. Make at least one new function call that includes the      #
#   number of tracks on an album.                                       #
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

