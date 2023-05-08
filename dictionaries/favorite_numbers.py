# Printing the values of each corresponding keys
numbers = {
    'Peter': 30,
    'Nick': 40,
    'Fiifi': 10,
    'Obed': 50,
    'Sylvia': 13,
}
#print("Peter's favorite number is " + str(numbers['Peter']))
#print("Nick's favorite number is " + str(numbers['Nick']))
#print("Fiifi's favorite number is " + str(numbers['Fiifi']))
#print("Obed's favorite number is " + str(numbers['Obed']))
#print("Sylvia's favorite number is " + str(numbers['Sylvia']))

for number in numbers.values():
    print(number)