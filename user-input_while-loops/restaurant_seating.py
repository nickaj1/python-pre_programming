# Taking
user = input('How many people are in your Dinner group? ')
user = int(user)
if user > 8:
    print('You would have to wait for a table.')
else:
    print('Your table is ready.')
print(user)