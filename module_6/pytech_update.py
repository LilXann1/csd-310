# Imports
from pymongo import MongoClient

# Connecting to MongoDB, MongoDB Cluster, and pytech database
url = url = 'mongodb+srv://admin:admin@cluster0.zkuaeue.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech

# Going to students collection and find all students in the collection 
students = db.students
student_list = students.find({})

# Display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Lavine"}})

# find the updated student document 
thorin = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
