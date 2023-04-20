# This code store a list of items and print series of statement about the list items.

cars = ['Porsche', 'Lamborghini', 'Ferrari', 'Rolls Royce', 'Dodge']
statement = 'I would like to own a ' + cars[0]  + ' car in future'
print(statement)

statement = 'I saw a red ' + cars[1] +' '+ 'car last week at my school'
print(statement)

statement = cars[2] + ' '+ 'Is one of the best car i have ever seen'
print(statement)

statement = 'A friend of mine drives a ' + cars[3] +' '+ 'to church every sunday.'
print(statement)

statement = 'My dad bought me a new ' + cars[4] +' '+ 'on my birthday'
print(statement)

# Appended a new element and printed a statement
cars.append('McLaren')
statement = cars[5] +' '+ 'is very expensive'
print(statement)