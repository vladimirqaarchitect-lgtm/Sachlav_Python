# immutable:
# string, bool, int,float,tuple, none, range

# mutable:
# list, dictionary, set, user-defined classes

# variables and objects:
#
# variable is a link to object in the memory


my_number = 20
print(id(my_number))

my_string = 'abc'
print(id(my_string))

my_number = 20
print(id(my_number))

other_number = my_number
print(id(other_number))

my_name = "bogdan"
print(id(my_name))

my_num = 100

print(id(my_num))

other_num = my_num

print(id(my_num))
