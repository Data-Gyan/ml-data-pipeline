import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        mongodburl = os.getenv('MONGODB_URL')
        secret = os.getenv('MONGODB_SECRET')
        mongodburl = mongodburl.format(os.getenv('MONGODB_SECRET'))

        self.client = pymongo.MongoClient(mongodburl,tlsCAFile=ca)
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
