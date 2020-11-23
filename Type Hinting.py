# Type hinting in Python
def printAge(age:int) -> str:
    '''
    Function take integer age and return string
    Note that this is just a hint and python no way forces the type. 
    This is to just help the development process. Person looking at the function will have an understanding
    of what is expected. 
    Look at typing module for more info
    https://docs.python.org/3.5/library/typing.html#module-typing
    '''
    return f"Your Age is {age}"

print(printAge(12))