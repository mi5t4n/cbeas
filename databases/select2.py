from sqlalchemy import create_engine, MetaData, Table, select, and_

# Create engine.
engine = create_engine('sqlite:///school.sqlite')

# Make database connection.
connection = engine.connect()

# Get metadata instance
metadata = MetaData()

# Get reference to users table
UsersTable = Table('Users', metadata, autoload = True, autoload_with = engine)

# Generat the SQL command.
usersSql = select([UsersTable.c.id, UsersTable.c.firstname ])
# usersSql = select([UsersTable.c.id, UsersTable.c.sex.label('Gender') ])
# usersSql = select([UsersTable]).where(UsersTable.c.sex == 'F')
# usersSql = select([UsersTable]).where(UsersTable.c.firstname.ilike('S%'))
# usersSql = select([UsersTable]).where(and_(UsersTable.c.firstname.ilike('S%'), UsersTable.c.sex == 'M'))

# Execute the command.
resultProxy = connection.execute(usersSql)

# Get the results.
results = resultProxy.fetchall()

print(results)