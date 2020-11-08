# In this one, I shall look at the important dunder methods of class
class SampleClass():
    ''' This is just a sample class! '''

    def __init__(self):
        self.name = 'Ajay'

    def __eq__(self, obj):
        return self.name == obj.name

    def __str__(self):
        return f"Just the way of printing {self.name}"


# The type of a class is 'type' itself
# print(type(SampleClass))

# all the methods a class has
# print(dir(SampleClass))

# Defining an object of class
obj = SampleClass()

# returns the module name| __main__ in this case
print('__module__ :: ', obj.__module__)
# constructor does always return None | Can't return anything from a __init__
print('__init__() :: ', obj.__init__())
print('__doc__ :: ', obj.__doc__)  # return the class Docstring

obj1 = SampleClass()
# We have defined what it would mean for the objects to be equal
print('__eq__() :: ', obj.__eq__(obj1))
# Getting the attribute value of an object
print('__getattribute__("name") :: ', obj.__getattribute__('name'))
# Displaying object data using __str__| __repr__ is more or less like __str__obj
print('__str__ :: ', obj)
# __size__of return 8 bytes for every additional character
print('__sizeof__() ::', obj.__sizeof__())
