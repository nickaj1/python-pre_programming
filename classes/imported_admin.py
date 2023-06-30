from privileges import User, Admin, Privilages


# Making Admin class instance
user_admin = Admin('Nick','Anderson','nickaj1505@gmail.com','Accra, GE-133-1487','Ghana')

# Calling method from the inherited Admin class
user_admin.privileges.show_privileges()