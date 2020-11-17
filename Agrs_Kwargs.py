# Agrs and Kwargs for arbitary number of agruements

# Agrs takes n number of non-keyword agruements and several operations can be performed with it then
def an_agrs_func(*agrs):
    val=0
    for a in agrs:
        val+=a
    return val

print(an_agrs_func(3,4,5))

# kwargs returns a dict which can be used to create some objects
class Developer:
    def __init__(self, **kwargs):
        for kwarg in kwargs:
            self.kwarg=kwargs[kwarg] # assigning key as value

new_developer=Developer(name='Vinay',age=26, role='Backend Engineer')
print(new_developer)

