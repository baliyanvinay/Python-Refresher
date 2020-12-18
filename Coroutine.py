# Execution of coroutine function begins only when next is called on coroutine t.
# This results in the execution of all the statements till a yield statement is encountered.
# Further execution of function resumes when an input is passed using send, and processes all statements till next yield statement.

def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper

@coroutine_decorator
def TokenIssuer(tokenId = 0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is ', tokenId)

t = TokenIssuer(100) # initialized the start
# next(t) #Decorator is used in this place
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close() # When coroutine t is closed, statements under GeneratorExit block are executed.