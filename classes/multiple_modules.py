# Importing Admin class from privilages_admin module
from privileges_admin import Admin


# Declaring Admin instance and calling method 
user_admin = Admin('Admin can add post','Admin can delete post','Admin can ban user','Admin can add story','Admin can send message')
user_admin.privileges.show_privileges()
