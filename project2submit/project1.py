import pymongo
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import datetime


class AnimalShelter:

    def __init__(self):
        

        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:47684/AAC' % ('aacuser', 'password'))

        self.db = self.client.AAC

        self.collection = self.db.animals

    def create(self, data):
        data_stored = None

        if data is not None:
            self.collection.insert_one(data)
        else:
            raise Exception("Nothing to save, data is empty")

        if self.collection.count_documents({'animal_id': 'A555555'}, limit=1) != 0:

            data_stored = 'True'

        else:

            data_stored = 'False'

        print('Data insert ', data_stored)

    def read(self, query_type):

        info = self.collection.find({query_type})

        return info
    
    def readAll(self, query_name):  
        
        
        return self.collection.find(query_name,{"_id":False})
    
    
   

    def update(self):
        query_to_update = input('Enter animal_id to update ')
        to_change = input('Enter what you are changing Ex name ')
        info_to_change = input('Enter change ')

        update_animal = {'animal_id': query_to_update}
        updated_info = {"$set": {to_change: info_to_change}}
        self.collection.update_one(update_animal, updated_info)
        return update_animal

    def delete(self):

        query_to_delete = input('Enter anmial_id to delete ')
        to_delete = {'animal_id': query_to_delete}
        self.collection.delete_one(to_delete)

        if self.collection.count_documents({'animal_id': query_to_delete}, limit=1) != 0:

            data_stored = 'False'

        else:

            data_stored = 'True'

        print('Data Delete ', data_stored)


