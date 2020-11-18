# Agrs and Kwargs for arbitary number of agruements

# Agrs takes n number of non-keyword agruements and several operations can be performed with it then
def an_agrs_func(*agrs):
    val=0
    for a in agrs:
        val+=a
    return val

print(an_agrs_func(3,4,5))

# Use of Kwargs
def display_details(**kwargs):
    for key, val in kwargs.items(): # since this is a dictionary object
        print(f'{key}: {val}')

display_details(name='Vinay', role='Backend Engineer')
