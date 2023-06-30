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


# Creating instances of the class
ghanaian = User('Kwadwo','Anim','nickaj1505@gmail.com','Accra, GE-133-1487','Ghana')
british = User('John','Smith','123 High Street, London, England','john.smith@example.com',' British')
american = User('Newt','Smith','123 Main Street, Anytown, USA','john.smith@example.com','American')

# Calling both methods of each user
# Method 1
ghanaian.describe_user() 
ghanaian.greet_user()

# Method 2
british.describe_user()
british.greet_user()

# Method 3
american.describe_user()
american.greet_user()


