from pymongo import MongoClient
from src.shared import MetaSingleton
from src.settings import DATABASE_HOST, DATABASE_PORT, DATABASE_USERNAME, DATABASE_PASSWORD


class DB(metaclass=MetaSingleton):
    @staticmethod
    def db_connection():
        # Define connection string for the database
        client = MongoClient(host=DATABASE_HOST, port=int(DATABASE_PORT), username=DATABASE_USERNAME,
                             password=DATABASE_PASSWORD)
        db = client['twitter']
        return db


databaseConnection = DB().db_connection()
