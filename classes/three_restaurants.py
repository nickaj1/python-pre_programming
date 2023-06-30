class Restaurant():
    '''Defining initailizer method'''
    def __init__(self,restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    # Defining method 1
    def describe_restaurant(self):
        print('Restaurant name:', self.restaurant_name)
        print('Cuisin type:', self.cuisine_name)

     # Defining method 2
    def open_restaurant(self):
        print(self.restaurant_name, 'is Open')

# Creating three instances of the class
restaurant = Restaurant('AJ Fast Food', 'Local Dishes')
my_cook = Restaurant('N&D Restaurant', 'French Cuisine')
eat_well = Restaurant('Eat Well', 'American Cuisine')

# Calling describe_restaurant() for each instance.
restaurant.describe_restaurant()
my_cook.describe_restaurant()
eat_well.describe_restaurant()
     

    
    
    

    
    
    


