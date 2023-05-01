# Using if-else chain to print statement of passed conditional test 
alien_colors2 = 'blue','white','red','pink','green'

if 'blue' in alien_colors2:
    print('Great! You earned 5 points.\n')


# If statement that print true statement
if 'yellow' not in alien_colors2:
    print('Nice! You earned 10 points.\n')


# if-else chain that print true statement
if 'white' and 'red' in alien_colors2:
    print('Congratulations! You earned 20 points.\n')

else:
    print('Opps... Try again next time')


# if-else chain that print false statement
if 'gray' in alien_colors2:
    print('Welldone, You earned 30 points')

else:
    print('Opps...Try again')