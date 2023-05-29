# Defining a function with a default paramters  

def make_shirt(slogan ,size='large'):
    '''Display message'''
    print('The slogan on the shirt is '+ slogan)
    print('The size of the shirt is ' + size)


# Calling function
make_shirt('I love Python')

# Modifying default paramter 
make_shirt('Look Good', size='medium')