# This store a person's name, Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

fname = "' Christain '\t"
lname = "' Addy '"
person_name = (fname + lname)
# Stripping with lstrip()
print(person_name.lstrip())

# Stripping with rstrip()
print(person_name.rstrip())

# Stripping with strip()
print(person_name.strip())