# Defining a function mixing Positional and Arbitrary Keyword Argument
def build_profile(first_name,last_name,**user_info):
    '''Display information of the user'''
# Declaring a dictionary which stores user info

    profile = {}
    profile['first_name'] = 'Nick'
    profile['last_name'] = 'Anderson'

# Looping through the arbitrary parameter

    for key, value in user_info.items():
        profile[key] = value

    return profile 

# Calling the function and passing Positional and Arbitrary argument
output = build_profile('Nick','Anderson', residence ='Accra', field ='Software Eng', language ='Python')
print(output)