# Importing module random which contains functions that generate random numbers
from random import randint
x = randint(1, 6)

class Die():

   def __init__(self,sides=6):
    self.sides = sides


   def roll_die(self):
      for self.sides in range(1,7): 
       if self.sides:
         print('Rolled score:', self.sides)
       

my_roll = Die()
my_roll.roll_die(10)
    
    
        
