# Defining a function that stores information in a Dictionary
def car(name,**model):
    '''Display information about car'''
    about_car = {}
    about_car['Name'] = name

# Looping through the arbitrary parameter
    for key, value in model.items():
        about_car[key] = value

# Printing dictionary making sure all the information is stored correctly
    print(about_car)

# Returning dictionary   
    return about_car


# Calling function with Arbirary Keyword
output = car('Porsche',model='911 Turbo',type='Carrera S',year='2023',color= 'Gray',price= '$220,000') 
print(output)





