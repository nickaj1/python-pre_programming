# Tests for equality and inequality 
# equality
cars = 'Porsche'
if 'Porsche' == cars:
    print(cars == 'Porsche')
    print('The best car i have ever seen\n')

# Inequality
if 'porsche' != cars:
    print(cars != 'porsche')
    print('Is not avialable\n')

# using the lower() function
    print(cars.lower() == 'porche')
    print('This is not my best type of car.\n')


# Numerical tests
forms1 = 18
forms2 = 23
print(forms1 == forms2)
print('The nums do not match.\n')


print(forms1 != forms2)
print('Not eligible.\n')


# greater than test printing true or false with string
print(forms2 > forms1)
print('Eligible.\n')

print(forms1 > forms2)
print('Go home.\n')


# less than test printing true or false with string
print(forms1 < forms2)
print('Subcribe.\n')

print(forms2 < forms1)
print('Go back and subcribe.\n')


# greater than or equal to printing true or false with string
print(forms1 >= forms2)
print('Not qualified.\n')

print(forms2 >= forms1)
print('Qualified.\n')


# less than or equal to printing true or false with string
print(forms1 <= forms2)
print('Sign in.\n')

print(forms2 <= forms1)
print('Sign up.\n')


# Using the 'and' keyword printing true or false with string
print(forms1 >= 23 and forms2 <= 18)
print('Opps....\n')

print(forms1 <= 23 and forms2 >= 18)
print('You made it.\n')


# Using the 'or' keyword printing true or false with string
print(forms1 <= 20 or forms2 >= 18)
print('Congratulation.\n')

print(forms1 >= 23 or forms2 <= 18)
print('Eliminated.\n')


# Using the 'in' keyword printing true or false with string
orders = ['rice','pizza','yam']
order = 'cheese'
print(order in orders)
print('Decline.\n')

print('rice' in orders)
print('Accepted.\n')


# Using the 'not in' keyword and printing a string
if order not in orders:
 print('Try again.\n')

if 'rice' not in order:
 print('Good job.\n')

