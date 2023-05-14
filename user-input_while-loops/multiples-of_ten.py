#
user = input('Enter a which is a multiple of 10')
user = int(user)
while user:

    if user % 10 == 0:
        print('Welldone! this number is a multiple of 10')

    else:
        print('Sorry, this number is not a multiple of 10')
        break
    

