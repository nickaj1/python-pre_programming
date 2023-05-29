# Defining a function 

def names_city(city,country):
    '''Return a simple value'''
    input = city + ' ' + country
    return input

# Calling the function
output = names_city('Accra,','Ghana')
print(output)

# Calling function with at least three city-country pairs
output = names_city(city='London,', country='United Kingdom')
print(output)

output = names_city(country='Nigeria', city='Abuja,')
print(output)

output = names_city('Kumasi,', country='Ghana')
print(output)

