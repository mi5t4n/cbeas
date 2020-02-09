from sqlalchemy import create_engine, MetaData, Table, select

# Create engine.
engine = create_engine('sqlite:///school.sqlite')

# Make database connection.
connection = engine.connect()

# Get metadata instance
metadata = MetaData()

# Get reference to users table
UsersTable = Table('Users', metadata, autoload = True, autoload_with = engine)

# Generat the SQL command.
usersList = select([UsersTable])

# Execute the command.
resultProxy = connection.execute(usersList)

# Get the results.
results = resultProxy.fetchall()

print(results)

# Get first row
firstRow = results[0]

# Display first row.
print(firstRow)

# Display the columns.
print(firstRow.keys())

# Display the firstname.
print(firstRow.firstname)