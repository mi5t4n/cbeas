from sqlalchemy import create_engine, MetaData, Table

# Create engine.
engine = create_engine('sqlite:///school.sqlite')

# Make database connection.
connection = engine.connect()

# Get metadata instance
metadata = MetaData()

# Get reference to users table
UsersTable = Table('Users', metadata, autoload = True, autoload_with = engine)

# Create insert command
userInsert = UsersTable.insert().values(firstname="Amit", lastname="Shah", age=22, sex="M")

# Execute the insert command.
connection.execute(userInsert)