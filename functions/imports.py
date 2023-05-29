# Importing functions and calling functions using different approach
# Using import module_name approach
import cars

# Calling function in module cars with dot
cars.output


# Using from module_name import function_name approach
from cars import car

# Calling function
car


# Using from module_name import function_name as fn(Alias) approach
from album import make_album as mka

# Calling function 
mka


# Using Import module_name as Alias
import sandwiches as sw

# Calling function in module of sandwiches with dot
sw.making_sandwich


# using from module_name import *
from great_magicians import *

# Calling functions in the module of great_magicians
show_magicians
make_great

