MongoDB: find() Example 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() Example 
doc = db.collection_name.find_one({“student_id”: “1007”})