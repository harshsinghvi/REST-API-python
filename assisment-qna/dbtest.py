import pymongo
import creds
import pprint

client = pymongo.MongoClient(creds.MONGO_DB_URI).app
db = client.todo

pprint.pprint(db.find_one())
print(db.find_one())
# for i in db.find({"pr":"1"}):
#     print(i['name'])