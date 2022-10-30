from pymongo import MongoClient
from src.shared import MetaSingleton


class DB(metaclass=MetaSingleton):
    @staticmethod
    def db_connection():
        # Define connection string for the database
        connection_string = "mongodb://twitter:twitter123@localhost:27017/twitter"
        client = MongoClient(connection_string)
        # TODO database connection
        return client
