# Generator are iterators and functions in python very good for enforcing sequence

def customContextManager():
    '''
    Function to enforce that a connection is established before a table is accessed
    '''
    print('Connection Established')
    yield
    print('Connection Closed')
    yield


def openDBtable():
    con = customContextManager()
    con.__next__()
    print('Table Opened')
    con.__next__()


openDBtable()
