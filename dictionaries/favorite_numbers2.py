numbers = {
    'Peter': [30,40,20,10,12],
    'Nick': [2,4,6,8,10],
    'Fiifi': [1,3,6,9,11,22],
    'Obed': [4,8,12,100,123],
    'Sylvia': [11,22,33,44,55,66,77,88,99,00],
}

# Looping through the dictionary
for name, number in numbers.items():
    print(name)
    for number in number:
        print(number)