# Dictionary for person 1
person1 = {
    "name": "John Smith",
    "age": 35,
    "gender": "Male",
    "occupation": "Software Engineer",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "phone": "555-555-1234"
}

# Dictionary for person 2
person2 = {
    "name": "Jane Doe",
    "age": 28,
    "gender": "Female",
    "occupation": "Marketing Manager",
    "address": {
        "street": "456 Oak St",
        "city": "Sometown",
        "state": "NY",
        "zip": "54321"
    },
    "phone": "555-555-5678"
}

# Dictionary for person 3
person3 = {
    "name": "Bob Johnson",
    "age": 42,
    "gender": "Male",
    "occupation": "Accountant",
    "address": {
        "street": "789 Elm St",
        "city": "Othertown",
        "state": "TX",
        "zip": "67890"
    },
    "phone": "555-555-9012"
}

# A list of Dictionaries
peoples = [person1,person2,person3]

# looping through the list
for people in (peoples):
    print(people)