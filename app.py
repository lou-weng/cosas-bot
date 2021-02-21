import pymongo

url = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(url)

# create a database called test
# you need at least 1 collection and 1 document for a database to be created
db = client['test']

# create a collection called people
collection = db['people']

dict = { "name": "Bob", "age": 20 }

result = collection.insert_one(dict)

print(client.list_database_names())
print(db.list_collection_names())
print(result.inserted_id)

