# Defining a function and passing a List to the function

def show_magicians(names):
    '''Display each magician name'''

    # Looping through the parameter
    for name in names:
        print('Hello, You are a great magician ' + name)

    # Making the list of magicians
magicians = ['David Wilt','Bruno Mayas','Wallcot Andrew','Mavis Lincon']

    # Calling the function
show_magicians(magicians)
