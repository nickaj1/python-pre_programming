# Using Dictionary to store a person information
person = {
    'first_name': 'Nick',
    'last_name' : 'Anderson',
    'age': 23,
    'city': 'Accra',
    }

# Added a new key-value pair
person['gender'] = 'male'
print(person)

# Looping through the dictionary
for name, detail in person.items():
    print('Info: ' + name)
    print('Ans ' + str(detail))