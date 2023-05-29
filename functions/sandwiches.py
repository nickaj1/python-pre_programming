# Denfining a function and passing an arbitrary number of arguments
def making_sandwich(*items):
    '''Display items for the sandwich'''
    print('Recipe for sandwish: ')
    for item in items:
        print(item)

# Calling function argument three times printing different argument
making_sandwich('Bread','Cheese','Pepper','Pickles','Salt','Chicken\n')
making_sandwich('Baguette','Turkey','Mustard','Lettuce','Bacon\n')
making_sandwich('Rolls','Deli meats','Mayonnaise','Cucumber','Avocado','Oregano','Hard-boiled eggs\n')


