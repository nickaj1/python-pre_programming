# Removing all Instances of specific values from a list
sandwich_orders = ['turkey club', 'BLT','pastrami','roast beef','pastrami','grilled cheese', 'ham and cheese', 'vegetarian', 'pastrami']
finished_sandwiches = []

print("Big Cups has run out of 'Pastrami'\n")

# Looping through the dulipcate value to remove any
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)
    if 'pastrami' not in sandwich_orders:
        break
    else: 
        continue



#Appending list to an empty list
orders = sandwich_orders
print(orders)
finished_sandwiches.append(orders)


# Looping through the list
for finished in finished_sandwiches:
     print(finished)
