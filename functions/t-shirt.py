# Defining a function and calling the function in both Positioning and Keyword argument

def make_shirt(size, slogan):
    '''Display message'''
    print('The size of the shirt is ' + size)
    print('The slogan on the shirt is ' + slogan)


# Calling the function using Positional argment
make_shirt('Large', 'Enjoy Yourself')

# Calling the function using Keyword argument
make_shirt(size='Large', slogan='Be Yourself')