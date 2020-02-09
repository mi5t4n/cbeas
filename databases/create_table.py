from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.types import Integer, Unicode, UnicodeText
from sqlalchemy.schema import ForeignKey

# Get engine.
engine = create_engine('sqlite:///school.sqlite')

# Get metadata.
metadata = MetaData()

# Define teachers table schema.
teachersTable = Table('Teachers', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', Unicode(255)),
                Column('subject', Unicode(255)))

# Create table.
metadata.create_all(engine)