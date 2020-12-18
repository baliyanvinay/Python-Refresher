# Execution of coroutine function begins only when next is called on coroutine t.
# This results in the execution of all the statements till a yield statement is encountered.
# Further execution of function resumes when an input is passed using send, and processes all statements till next yield statement.

def TokenIssuer():
    tokenId = 0
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is ', tokenId)

t = TokenIssuer(100) # initialized the start
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()