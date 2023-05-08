glossary = {
    'List': 'A list is a collection of items that are ordered and changeable.',
    'Tuple': 'A tuple is similar to a list, but it is immutable, meaning that its contents cannot be modified once it is created.',
    'Function': ' A function is a block of code that performs a specific task. It takes input (arguments) and returns output (return value) if any.',
    'Dictionary': ' A dictionary is a collection of key-value pairs that are unordered and changeable',
    'Conditional Statement': 'A conditional statement is a type of control structure that allows a program to execute different code based on whether a condition is true or false.',
    'Class': 'A class is a blueprint for creating objects that have similar properties and methods.',
    'Module': 'A module is a file containing Python code that can be imported into another Python script',
    'Loop': 'A loop is a programming construct that allows a block of code to be executed repeatedly.',
}
# Looping through the dictionary
for term , definition in glossary.items():
    print('Term: ' + term)
    print('Definition: ' + definition)