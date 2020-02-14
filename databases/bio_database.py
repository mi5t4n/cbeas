from sqlalchemy import create_engine, MetaData, Table, select, and_

engine = create_engine('sqlite:///school.sqlite')

# print(engine.table_names())
metadata = MetaData()

studentTable = Table('Student', metadata, autoload = True, autoload_with = engine)

# Create insert query.
# insertSql = studentTable.insert().values(name='Sumit', age=22, rollno=100)
# print(insertSql)

# Create select query
# selectQuery = select([studentTable])
# selectQuery = select([studentTable.c.name, studentTable.c.rollno])
# selectQuery = select([studentTable.c.name]).where(studentTable.c.rollno == 45)
# selectQuery = select([studentTable]).where(studentTable.c.name.ilike('A%'))
# selectQuery = select([studentTable]).where(and_(studentTable.c.name.ilike('S%'), studentTable.c.rollno == 6))

# updateQuery = studentTable.update().where(studentTable.c.name == 'Suman').values(age=30)

deleteQuery = studentTable.delete().where(studentTable.c.name == 'Suman')

# print(repr(studentTable))

connection = engine.connect()

# connection.execute(insertSql)

# Execute the select query
connection.execute(deleteQuery)

# Fetch all the records.
# students = resultProxy.fetchall()

# print(students)
# length = len(students)

# for index in range(0, length):
#     student = students[index]
#     print (student['name'])

# firstStudent = students[0]

# print(firstStudent)
# print(firstStudent['name'])