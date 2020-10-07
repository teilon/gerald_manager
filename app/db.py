import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

POSTGRES_HOST = '84.38.181.88'  # os.environ['POSTGRES_HOST']
POSTGRES_PORT = '5432'  # os.environ['POSTGRES_PORT']
POSTGRES_DATABASE = 'geralddb'   # os.environ['POSTGRES_DB']
POSTGRES_USER = 'torn'  # os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = 'helicopter'    # os.environ['POSTGRES_PASSWORD']

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.\
    format(POSTGRES_USER,
           POSTGRES_PASSWORD,
           POSTGRES_HOST,
           POSTGRES_PORT,
           POSTGRES_DATABASE)
