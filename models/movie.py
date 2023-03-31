from config.database import Base
from sqlalchemy import Column , Integer , String, Boolean, Float

class Movie(Base): #heredo movies de base - será una entidad de mi base de datos

    __tablename__ = "movies" #nombre de la tabla
    id = Column(Integer, primary_key= True) # será una columna con contrint integer y será una llave primaria
    title = Column(String) 
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
    

    
