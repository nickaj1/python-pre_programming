# Defining a function with a default parameter

def items(brand,type,amount=0):
    '''Display list of items'''
    print('This is one of the best rating cars')
    showcase = {'Brand':brand, 'Type':type}

    if amount:
        showcase['Amount'] = amount
    
    return showcase
    
    
output = items('Porsche' , '911 Carrera S', '$210,000')
print(output)



# Second Approach


def items(brand,type,amount=0):
    '''Display list of items'''

    if amount:
        showcase = {'Brand':brand, 'Type':type, 'Amount': amount}
    
    else:
         showcase = {'Brand':brand, 'Type':type}

    return showcase


display = items('Porsche' , '911 Carrera GTS', '$230,000')
print(display)




    

    