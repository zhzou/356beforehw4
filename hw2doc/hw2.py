import os
import pymongo
from pprint import pprint
import json
from bson.json_util import loads

path = '/home/ubuntu/hw2doc'
client = pymongo.MongoClient('localhost',27017)
db = client['hw2']
factbook = db.factbook
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".json"):
            path_file = os.path.join(root,file)
            print(file)
            page = open(path_file,'r')
            d = loads(page.read())
            factbook.insert(d, check_keys = False)


#client = pymongo.MongoClient('mongodb://admin:1234@localhost.com:27017/')


