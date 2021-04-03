# Simplest way to create a Singleton class
class _Database_Connect:
    def __str__(self):
        return "Database Connected!"

_instance = None

def Database_Connect():
    global _instance
    if _instance is None:
        _instance = _Database_Connect()
    return _instance


# Overiding __new__ of class || There is only one govt in a country 
class Government:
    _instance = None
    def __new__(cls, country_name):
        if not cls._instance: # if cls._instance is None
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, country_name):
        self.country_name = country_name
    
    def __str__(self):
        return f"Government of {self.country_name}"


if __name__ == '__main__':
    db_con = Database_Connect()
    print(db_con)

    db_con_again = Database_Connect()
    print(db_con_again)

    print(db_con is db_con_again)

    # Government Singleton
    indian_govt = Government('India')
    bharat_govt = Government('India')
    print(indian_govt, ' ', bharat_govt)
    print(indian_govt is bharat_govt)
