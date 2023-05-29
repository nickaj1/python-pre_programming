# Defining a function with a default parameter for country

def describe_city(city , country='Ghana'):
    '''Display simple message'''
    print(city + ' is the capital of ' + country)

# Calling the function using the positonal argument
describe_city('Accra')

# Calling function for three different cities using the positional and keyword argument
describe_city('London', country='UK')
describe_city(city='Washington D.C', country='USA')
describe_city(country= 'Canada', city='Ottawa')
