# Taking user input into a dictionary and Printing the key-value pairs
intakes = {}

# Set a flag to make poll active
active = True

# Taking user input while flag is active (key-value pairs)
while True:
    name = input('What is your name?')
    response = input('If you could visit one place in the world, where would you go?')
 

# Set input into the dictionary (key-value pairs)
    intakes[name] = response

# Adding extra input while the loop is active
    repeat = input('Would you like to send another respond? (Yes/No)')
    if repeat == 'No':
        active = False


# Printing polling results (key-value pairs) in the Dictionary
    for name, response in intakes.items():
        print('Name: ' + name)
        print('Prefer to visit: ' + response)
        
    



