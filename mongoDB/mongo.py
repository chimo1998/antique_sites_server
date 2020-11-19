import pymongo
class Database:
    URL = "mongodb://localhost:27017/"
    DB_NAME = "antique"
    COL_NAME = "sensor"
    def __init__(self, url=URL, db_name=):
