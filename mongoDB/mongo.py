import pymongo
import json
class Database():
    URL = "mongodb://localhost:27017/"
    DB_NAME = "antique"
    COL_NAME = "sensor"
    def __init__(self, url=URL, db_name=DB_NAME, col_name=COL_NAME):
        self.url = url
        self.db_name = db_name
        self.col_name = col_name
        self.client = pymongo.MongoClient(self.url)
        self.db = self.client[db_name]
    def convert(self, data):
        temp = []
        if type(data) == list:
            for d in data:
                temp.append(json.loads(d))
        elif type(data) == str:
            temp.append(json.loads(data))
        else:
            print("Nothing to convert")
        return temp
    def insert(self, collection, data):
        col = self.db[collection]
        converted = self.convert(data)
        if len(converted) == 0:
            return 0
        return col.insert_many(converted)
