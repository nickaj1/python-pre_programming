rivers = {
    'Nile' : 'egypt',
    'Pra' : 'ghana',
    'jordan': 'isreal',
}
for name , destination in rivers.items():
    print('The river ' + name + ' runs through ' + destination)
print('\n')



# Printing each river in the dictionary 
for name in rivers.keys():
    print('These are the name of the rivers included in the dictionary: ' + name)
print('\n')

# Printing name of each country in the dictionary
for destination in rivers.values():
    print('These are the destination of the rivers: ' + destination)
