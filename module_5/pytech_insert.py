# Imports
from pymongo import MongoClient

# Connecting to MongoDB, MongoDB Cluster, and pytech database
url = url = 'mongodb+srv://admin:admin@cluster0.zkuaeue.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech

# Going to students collection and find all students in the collection 
students = db.students
student_list = students.find({})

# adam Smith's data document 
adam = {
    "student_id": "1007",
    "first_name": "Adam",
    "last_name": "Smith",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CIS310",
                    "description": "Database Security",
                    "instructor": "Professor Haas",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Haas",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# John Doe's data document 
john = {
    "student_id": "1008",
    "first_name": "John",
    "last_name": "Doe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CIS310",
                    "description": "Database Security",
                    "instructor": "Professor Haas",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Haas",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# Jane Doe's data document
jane = {
    "student_id": "1009",
    "first_name": "Jane",
    "last_name": "Doe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CIS310",
                    "description": "Database Security",
                    "instructor": "Professor Haas",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Haas",
                    "grade": "B"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
adam_student_id = students.insert_one(adam).inserted_id
print("  Inserted student record Adam Smith into the students collection with document_id " + str(adam_student_id))

john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Doe into the students collection with document_id " + str(john_student_id))

jane_student_id = students.insert_one(jane).inserted_id
print("  Inserted student record Jane Doe into the students collection with document_id " + str(jane_student_id))

input("\n\n  End of program, press any key to exit... ")