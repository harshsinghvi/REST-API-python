import pymongo
import creds
client = pymongo.MongoClient(creds.MONGO_DB_URI)
db = client.test

print(db)