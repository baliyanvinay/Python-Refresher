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

if __name__ == '__main__':
    db_con = Database_Connect()
    print(db_con)

    db_con_again = Database_Connect()
    print(db_con_again)

    print(db_con is db_con_again)
