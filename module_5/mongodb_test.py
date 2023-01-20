from pymongo import MongoClient

url = “mongodb+srv://admin:admin@cluster0.zkuaeue.mongodb.net/?retryWrites=true&w=majority”
client = MongoClient(mongodb+srv://admin:admin@cluster0.zkuaeue.mongodb.net/?retryWrites=true&w=majority)
db = client.pytech
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")
