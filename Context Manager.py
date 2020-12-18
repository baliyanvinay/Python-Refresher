# A Context Manager allows perform required activities, automatically, 
# while entering or exiting a Context.

class DBConnect(object):
    def __init__(self, dbname):
        self.dbname=dbname

    def __enter__(self):
        self.dbConnection=connect(self.dbname)
        return self.dbConnection
    
    def __exit__(self):
        self.dbConnection.close()

with DBConnect('OracleDB') as db:
    cursor=db.cursor()
    '''
    Perform Operations here
    '''
    # No need to close the connection here as contextManager(with) will close it on exit
    
