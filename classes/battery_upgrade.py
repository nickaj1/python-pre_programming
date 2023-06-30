#  Creating a Car() class with a Battery() class method 

class Car():
    '''Initializing attributes'''
    def __init__(self,name,type,model):
        self.name = name
        self.type = type
        self.model = model
        self.mph = 0

# Defining method for the class attributes    
    def get_car(self):
        print('Car Name:', self.name)
        print('Model:', self.model)
        print('Type:', self.type)
        
# Defining method for the default class attributes        
    def get_miles(self,miles):
        self.mph = miles
        print('Miles:', self.mph)


# Defining a Battery class method that checkes the battery size and set capacity to 85
class Battery():
 '''initializing attribute'''
 def __init__(self,battery_size = 70):
    self.battery_size = battery_size

# A method that set battery capacity to any size   
 def upgrade_battery(self,capacity):
  capacity = self.battery_size
  if capacity != 85:
     capacity = 85
  print('Battery capacity:' + str(self.battery_size))

 
 

# Inheriting the class Car() with Battery() class set as default 
class ElectricCar(Car):
    '''Initializing attributes'''
    def __init__(self, name, type, model):
        super().__init__(name, type, model)
        self.battery = Battery()

# Declaring a range method that ranges the car battery 
    def get_range(self):
        if self.battery == 70:
           return 180
        elif self.battery == 85:
           return 220


# Declaring instance of the inherited class             
my_car = ElectricCar('Tesla','S','2023')
my_car.get_car()
my_car.get_miles(10)
my_car.battery.upgrade_battery(85)
my_car.get_range()


              



    