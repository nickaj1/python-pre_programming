#
my_pizzas = ['margherita pizza', 'pepperoni pizza', 'hawaiian pizza', 'bbq chicken pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('spicy pizza')
friend_pizzas.append('beef pizza')
print(my_pizzas)
print(friend_pizzas)

for pizzas in  my_pizzas:
 print(pizzas)
print('These are my favorite pizzas\n')

for friends in friend_pizzas:
 print(friends)
print('My friends favorite pizzas')