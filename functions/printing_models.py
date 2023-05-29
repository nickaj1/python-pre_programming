# Defining a function with a robot specification

def auto_bot(first_name,last_name,**qualities):
    '''Display the info of the autobot'''
# Declaring a dictionary
    full_name = {}
    full_name['First Name'] = first_name
    full_name['Last Name'] = last_name

# Looping through the arbitrary key-value parameter
    for key, value in qualities.items():
        full_name[key]= value

# Returning dictionary name    
    return full_name

# Calling function
output = auto_bot('Autonomous','Bot',Sensor='Cameras',Decision_making='Data Analyza',Energy_Management='Rechargeable Batteries')
print(output)


