from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, registry
from . import config

host = config.db.get('HOST')
username = config.db.get('USERNAME')
password = config.db.get('PASSWORD')
database = config.db.get('DATABASE')

engine = create_engine(
    pool_size=100, 
    max_overflow=0,
    url = f'mysql+pymysql://{username}:{password}@{host}/{database}', 
)
session = scoped_session(sessionmaker(bind=engine), scopefunc=request)
mapper_registry = registry()
Base = mapper_registry.generate_base()