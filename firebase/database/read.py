import pyrebase

config = {
  "apiKey"           : "AIzaSyDWqZmqXJ8EOT8BhN2I_TM1JL9PrpJAdq0",
  "authDomain"       : "eloquent-drive-110521.firebaseapp.com",
  "databaseURL"      : "https://eloquent-drive-110521.firebaseio.com",
  "projectId"        : "eloquent-drive-110521",
  "storageBucket"    : "eloquent-drive-110521.appspot.com",
  "messagingSenderId": "917806153189",
  "appId"            : "1:917806153189:web:b4f1782fcfdb0bad53030c",
  "measurementId"    : "G-5X20RHBLP4"
};

firebase = pyrebase.initialize_app(config)

db = firebase.database()


# Read all the students.

# def studentHandler(message):
#     print(message["event"])
#     print(message["path"])
#     print(message["data"])
# studentStream = db.child("students").stream(studentHandler)

# Display all the students
students = db.child("students").get()
for student in students.each() :
    print(student.key())
    print(student.val())

# Display student by roll no.
students = db.child("students").order_by_child("rollno").equal_to(45).get()
students = db.child("students").order_by_child("name").limit_to_first(1).get()
for student in students.each():
    print(student.key())
    print(student.val())

# sagar = {
#     "name" : "Sagar Subedi",
#     "rollno": 45,
#     "age": 20
# }

# db.child("students").push(sagar)