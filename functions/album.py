# Defining function that builds a dictionary

def make_album(artist_name,album_title,tracks_no=0):
    '''Return a dictionary containing three pieces of information if only user provides a value for optional else return two pieces of information'''
    if tracks_no > 0:
        f_album = {'artist': artist_name, 'album title':album_title, 'track_no':tracks_no}
    else:
        f_album =  {'artist': artist_name, 'album title':album_title}
         
    return f_album
    
     
# Calling function
check = make_album('Victoria Orenze','My Fortress',3 )
print(check)




# Defining a function with a dictionary representing different albums

def make_album(artist_name,artist_album):
    '''Return artist information well formated'''
    
    artist = {'artist':artist_name, 'album':artist_album}
    return artist


# Calling the function
output = make_album('Jay-Z','4:44')
print(output)




# Defining a function with a dictionary representing different albums
def make_album(artist_name,album_title,track_no=''):
    '''Return artist work neatly'''
    artist = {'artist':artist_name,'title':album_title}

# Adding an optional function to the dictionary if any
    if track_no:
        artist['track'] = track_no

    return artist

# Calling function of the dictionary
output = make_album('Remission Choir','Asem papa,Oye',5)
print(output)





