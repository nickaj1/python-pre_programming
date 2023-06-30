#Declaring a User class that displays detials of user
class User():
    '''Defining attribute of the class'''

    def __init__(self,first_name,last_name,email,address,country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.country = country

# Defining method
    def describe_user(self):
        print('Hi, my name is', self.first_name, self.last_name)
        print('I am from', self.country)
        print('My address', self.address )
        print('You can reach out to me on', self.email)

# Defining method 2
    def greet_user(self):
        print('\nGood Morning', self.first_name, self.last_name)


