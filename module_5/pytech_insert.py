MongoDB: insert_one()
fred = {
 “first_name”: “Fred”
}
 
fred_student_id = students.insert_one(fred).inserted_id
 
print(fred_student_id)