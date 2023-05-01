# Using if-elif-else chain to print conditional test and statement in three versions
# Version 1
alien_colors3 = 'blue','white','red','pink','green','brown'
if 'green' in alien_colors3:
    print('You earned 5 points.')

elif 'green' not in alien_colors3:
    print('Try again.')

else: 
    print('Opps...')


if 'white' in alien_colors3:
    print('You won 10 points.')

elif 'white' not in alien_colors3:
    print('Sorry, Try again.')
 
else: 
    print('Opps...') 


if 'pink' in alien_colors3:
    print('Congratulations, You won 15 points.\n')

elif 'pink' not in alien_colors3:
    print('Sorry, Try again')

else:
    print('Opps...')


# Version 2
if 'blue' not in alien_colors3:
    print('You missed this one.')

elif 'blue' in alien_colors3:
    print('Great job, You earned 5 points.')

else:
    print('Opps...')


if 'red' not in alien_colors3:
    print('You missed the shot.')

elif 'red' in alien_colors3:
    print('Good, You earned 10 points.')

else:
    print('Opps')


if 'white' not in alien_colors3: 
    print('Try again')

elif 'white' in alien_colors3:
    print('Awesome, You won 15 points.\n')

else:
    print('Opps...')


# Version 3
if 'purple' in alien_colors3:
    print('Nice, You have won 5 points.')

elif 'gray' in alien_colors3:
    print('Nice, You have won 10 points')

else: 
    print('Welldone, You have won 5 points.')


if 'ash' in alien_colors3:
    print('You lost a point')

elif 'orange' in alien_colors3:
    print('Try again')

else:
    print('Awesome, you earned 10 points.')


if 'black' in alien_colors3:
    print('Find it please')

elif 'sea blue' in alien_colors3:
    print('Are you sure?')

else: 
    print('Congratulations, You earned 15 points.')

