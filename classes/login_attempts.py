class User():
    '''Defining attribute of the class'''

    def __init__(self,first_name,last_name,email,address,country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.country = country
        self.login_attempts = 3

# Defining method 1
    def describe_user(self):
        print('Hi, my name is', self.first_name, self.last_name)
        print('I am from', self.country)
        print('My address', self.address )
        print('You can reach out to me on', self.email)
        print('Login attempt', self.login_attempts , '\n')

# Defining method 2
    def greet_user(self):
        print('\nGood Morning', self.first_name, self.last_name)

# Defining method that increments the value of login_attempts by 1
    def increment_login_attempts(self,add):
        '''Increment value by 1'''
        self.login_attempts += add
        

# Defining method resets the value of login_attempts to 0.
    def reset_login_attempts(self,reset):
        '''Reset value of login'''
        self.login_attempts = reset
      
        



# Creating instances of the class
ghanaian = User('Kwadwo','Anim','nickaj1505@gmail.com','Accra, GE-133-1487','Ghana')
british = User('John','Smith','123 High Street, London, England','john.smith@example.com','England')
american = User('Newt','Smith','123 Main Street, Anytown, USA','john.smith@example.com','USA')

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

# Calling Increment_login_attempts() several times.
ghanaian.increment_login_attempts(3)
ghanaian.describe_user()

british.increment_login_attempts(6)
british.describe_user()

american.increment_login_attempts(5)
american.describe_user()


# Calling reset_login_attempts() method making sure it reset login_attempts attribute to 0.
ghanaian.reset_login_attempts(0)
ghanaian.describe_user()

british.reset_login_attempts(0)
british.describe_user()

american.reset_login_attempts(0)
american.describe_user()