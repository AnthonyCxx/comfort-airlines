from sqlalchemy import create_engine, MetaData
from eralchemy2 import render_er


database_url = 'mariadb+mariadbconnector://root:toor@172.17.0.1:3306/comfort_airlines_db'
engine = create_engine(database_url)

metadata = MetaData()

# Reflect the database schema
metadata.reflect(bind=engine)

# Show ER model from here
render_er(metadata, 'thing.png')
