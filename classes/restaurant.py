class Restaurant():
    '''Defining initailizer method'''
    def __init__(self, restaurant_name, cuisine_type ):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type

    def describe_restaurant(self):
     '''Display information about restaurant'''
     print('The name of my restaurant is' , self.restaurant_name)
     print('Cuisine type for our restaurant is' , self.cuisine_type)

    def open_restaurant(self):
     '''Display time and days restaurants is open'''
     print(self.restaurant_name , 'is currently open')

# Creating an instance of the Restaurant class
restaurant = Restaurant('AJ Restaurant', 'Seafood')

# Printing the attributes individually
print('The name of my restaurant is',restaurant.restaurant_name  )
print('Our cuisine type is' , restaurant.cuisine_type)

# Calling method
restaurant.describe_restaurant()
restaurant.open_restaurant()