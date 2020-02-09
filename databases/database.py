from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///school.sqlite')

metadata = MetaData()

users = Table('Users', metadata, autoload = True, autoload_with = engine)

print(repr(users))