# Imports
from pymongo import MongoClient

# Connecting to MongoDB, MongoDB Cluster, and pytech database
url = url = 'mongodb+srv://admin:admin@cluster0.zkuaeue.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech

# Going to students collection and find all students in the collection 
students = db.students
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
bilbo = students.find_one({"student_id": "1008"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + bilbo["student_id"] + "\n  First Name: " + bilbo["first_name"] + "\n  Last Name: " + bilbo["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")