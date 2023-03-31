from pydantic import BaseModel, Field #para validar datos field
from typing import Optional, List #para indicar que un parametro es opcional pero de otra forma, list es para devolver listas como respuestra con response_model


#creacion de esquema de datos
class Movie(BaseModel):
    id: Optional[int] #puede ser opcional o entero
    title: str = Field(min_length= 5, max_length=30) #maximo de 15 digitos , se le añade un default
    overview: str = Field(min_length= 15, max_length=50)
    year: int = Field(le=2022) #Le = less than or equal
    rating: float = Field(ge= 1, le= 10.0)
    category: str = Field(max_length= 20)

    #añadiendo campos por defecto en otra clase
    class Config:
        schema_extra ={
            "example": {
            "id": 1,
            "title": "pelicula ###",
            "overview": "descripción pelicula",
            "year": 2022,
            "rating": 9.8,
            "category" : "horror"
            
            
            }
        }