# Object Printer
def print_object(var):
    print('Object {}'.format(var))
    print('ID of object: ', id(var))
    print('Type of object : ', type(var))
    print('Value of object : ', var)
    print('\n')

# Mutable data types in Python


# Immutable objects/data types in Python
var = 17  # Do note that the object here is 17 and not var, var is the variable holding object 17
print_object(var)

var = 89
print_object(var)

var = 'name'
print_object(var)

var = 78.0
print_object(var)

var = ('Grey', 17)  # a tuple
print_object(var)

var = ('Grey', 7)  # made changes in tuple
print_object(var)  # result will be a different ID
