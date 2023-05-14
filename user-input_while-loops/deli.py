# Moving a list to an empty list
sandwich_orders = ['turkey club', 'BLT', 'roast beef', 'grilled cheese', 'ham and cheese', 'vegetarian']

# Empty list
finished_sandwiches = []

# Looping through the main list
while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print('I made your ' + sandwiches)

# Appending main list to empty list
finished_sandwiches.append(sandwiches)
print(finished_sandwiches)
 
# Printing each name in the list
for finished in finished_sandwiches:
    print(finished)