# Defining a function and passing a List to the function
def show_magicians(names,infos):
    '''Display each magician name'''
    while names:
        name = names.pop()
        print('Hello '+ name)
# Appending names to info
        infos.append(name)

# Defining the function make_great() which modifies the list
def make_great(infos):
    '''Display each magician name'''
    # Looping through the parameter
    print('\nModifying the list:')
    for info in infos:
        print('Hello, The Great ' + info)

# Making the list of magicians

names = ['David Wilt','Bruno Mayas','Wallcot Andrew','Mavis Lincon']
infos = []
# Calling the function

show_magicians(names,infos)
make_great(infos)

