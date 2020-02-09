from sqlalchemy import create_engine, MetaData, Table, select, and_

# Create engine.
engine = create_engine('sqlite:///school.sqlite')

# Make database connection.
connection = engine.connect()

# Get metadata instance
metadata = MetaData()

# Get reference to users table
UsersTable = Table('Users', metadata, autoload = True, autoload_with = engine)

updateSql = UsersTable.update().where(UsersTable.c.firstname == 'Suman').values(firstname='Suraj')

connection.execute(updateSql)