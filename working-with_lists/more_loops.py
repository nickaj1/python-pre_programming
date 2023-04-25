# Two for loops to print each list of foods
my_foods = ['pizza', 'falafel', 'carrot cake', 'rice', 'yam']
friend_foods = my_foods[:]

my_foods.append('plantain\n')
friend_foods.append('waakye')

for my in my_foods:
    print(my)

for friends in friend_foods:
    print(friends)