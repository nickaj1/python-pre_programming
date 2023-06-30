class Restaurant():
    '''Defining initailizer method'''
    def __init__(self, restaurant_name, cuisine_type ):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
    # Adding an attribute called number_served with a default value of 0
      self.number_served = 10

    def describe_restaurant(self):
     '''Display information about restaurant'''
     print('The name of my restaurant is' , self.restaurant_name)
     print('Cuisine type for our restaurant is' , self.cuisine_type)
     print('Number of customers the restaurant has served', self.number_served)
    
    def open_restaurant(self):
     '''Display time and days restaurants is open'''
     print(self.restaurant_name , 'is currently open')

    def set_number_served(self,customers):
      '''Set the number of customers served'''
      if customers >= self.number_served:
         self.number_served = customers
      else:
        print('No customer was served.')
      print('Number currently served is:', self.number_served)

    def increment_number_served(self,add):
      '''increment the number of customers served'''
      self.number_served += add

      
# Creating an instance of the Restaurant class
# restaurant = Restaurant('AJ Restaurant', 'Seafood')

# Printing the attributes individually
# print('The name of my restaurant is',restaurant.restaurant_name  )
# print('Our cuisine type is' , restaurant.cuisine_type)

# Calling method
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.set_number_served(20)
# restaurant.increment_number_served(30)
# restaurant.describe_restaurant()


# Declaring a class(subclass) that inherits from the main or parent class

class IceCreamStand(Restaurant):
  '''Initializing Parent class and adding attribute in Subclass
  that stores a list'''
  def __init__(self,restaurant_name, cuisine_type):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = ['Banana','Apple','Strawberry']

# Declaring method that displays list in Subclass attribute
  def types_flavors(self):
    print('These are the flavors of ice cream available', self.flavors)

# Creating instance of the Subclass
my_restaurant = IceCreamStand('AJ Restaurant','French Ice Cream')

# Calling methods of Subclass and Parent class
my_restaurant.describe_restaurant()
my_restaurant.types_flavors()






    
    