# Importing imported_ad.py module for Admin class to inherite
from users import User


# Declaring both Privileges and Admin classes
class Privilages():
    '''Initializing attribute of the class'''
    def __init__(self):
        self.privileges = ['Admin can add post','Admin can delete post','Admin can ban user','Admin can add story','Admin can send message']
 
    
# Declaring method of the class
    def show_privileges(self):
        print('\nSet of Privilages:',self.privileges)


# Declaring a subclass with an instance as an attribute
class Admin(User):
    '''Initializing Parent class and adding attribute in Subclass
  that stores a list'''
    def __init__(self, first_name, last_name, email, address, country):
        super().__init__(first_name, last_name, email, address, country)
        self.privileges = Privilages()