import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite" # ../ significa que retroceda una carpeta
base_dir = os.path.dirname(os.path.realpath(__file__))

#creacion de URL
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#configuracion del motor de la db
engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()