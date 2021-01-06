# Object Printer
def print_object(var):
    print('Object {}'.format(var))
    print('ID of object: ', id(var))
    print('Type of object : ', type(var))
    print('Value of object : ', var)


# Mutable data types in Python
# Lists
var = [17, 10]
print_object(var)
var += [17]
print_object(var)
print('\n')

# Dictionary
var = {'first_name': 'Vinay', }
print_object(var)
var['last_name'] = 'Baliyan'
print_object(var)
print('\n')

# Set
var = {1, 2}
print_object(var)
var.update({2, 3})  # to add values in current set
print_object(var)
print('\n')

# Immutable objects/data types in Python
# Numeric values
var = 17.0  # Do note that the object here is 17 and not var, var is the variable holding object 17
print_object(var)
var += 10
print_object(var)
print('\n')

# Strings
var = 'Vinay'
print_object(var)
var += ' Baliyan'
print_object(var)
print('\n')

# Tupple
var = ('Grey',)
print_object(var)
var += (17,)  # made changes in tuple
print_object(var)  # result will be a different ID
print('\n')
