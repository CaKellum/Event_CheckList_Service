from os import getenv
from sqlite3 import connect

class DatabaseManager():
    def __init__(self) -> None:
        print("database manager made")
        self.__db_path = getenv('DB_PATH')
        self.__conection_counter = 0

    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseManager, cls).__new__(cls)
        return cls.instance
    
    def __get_connection__(self):
        self.__conection_counter += 1
        print(f"{self.__conection_counter} made connections in life of this manager")
        return connect(self.__db_path) 