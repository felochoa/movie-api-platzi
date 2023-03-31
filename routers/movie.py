from fastapi import APIRouter
from fastapi import Depends, Path, Query  #path: para validacion de parametros de ruta, query = validar parametros query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field #para validar datos field
from typing import Optional, List #para indicar que un parametro es opcional pero de otra forma, list es para devolver listas como respuestra con response_model
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

#creacion del router
movie_router = APIRouter()


#aqui reemplazamos @app por @movie_router



#clase para respuesta a errores 404 o otros ver https://fastapi.tiangolo.com/advanced/additional-responses/
class Message(BaseModel):
    message: str


####
#metodos para movies:


#metodo para que muestre todas las peliculas
@movie_router.get("/movies", tags = ["movies"], response_model= List[Movie], status_code= 200, responses={404: {"model": Message}}, dependencies= [Depends(JWTBearer())])

def get_movies() -> List[Movie]: #debemos especificar aca el tipo de respuesta tambien
    db = Session() #creanod la sesion 
    #restult = db.query(MovieModel).all() # aqui hago el query - en este caso me da todos los datos de las  peliculas
    
    result = MovieService(db).get_movies() #aqui se hace el servicio de query para todas las peliculas
    return JSONResponse(status_code =200, content= jsonable_encoder(result) )


#metodo filtrar por id
@movie_router.get("/movies/{id}", tags = ["movies"], response_model=Movie)  #añadiendo un  parametro de ruta por id, ademas añadimos la etiqueta , añadimos reponse model que solo envie una pelicula
def get_movie(id: int = Path(ge=1, le=9999)) -> Movie: #funcion que requiere de un id de tipo entero , añadimos validacion de path con id
    db = Session()
    result = MovieService(db).get_movie(id) #filtrar por id y dar el primer resultado .first
    
    if not result:
        return JSONResponse(status_code= 404, content= {"message": "no encontrado"})
    
    return JSONResponse(status_code= 200,  content= jsonable_encoder(result))
    
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content= item)

        
    return JSONResponse(content= [], status_code = 404, resp = {"message": "item not found" })

        
#filtrando peliculas por query por categoria
@movie_router.get("/movies/", tags = ["movies"], response_model= List[Movie], responses={404: {"model": Message}} ) #para que no se sobreescriba le añadimos una barra al final /
def get_movies_by_categories(category: str = Query(min_length=5, max_length= 15) ) -> List[Movie]:
    
    #filtrar por categorias con la base de datos
    db = Session()
    result = MovieService(db).get_movie_category(category) #filtrar por categoria y dar todos los resultados
    if not result:
        return JSONResponse(status_code= 404, content= {"message": "categoria no encontrada"})
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))




    ###########################################################
    #return category
    #matching_categories = []
#reto filtrar peliculas por categoria con el parametro query creado
    """ for titles in movies:
        if titles["category"] == category:
            matching_categories.append(titles) """
    matching_categories = [ titles for titles in movies if titles["category"] == category]

    if len(matching_categories) == 0:
        return JSONResponse(status_code= 404, content= {"message": "item not found" })
    else:
        return JSONResponse(content= matching_categories)


#usando el metodo post
@movie_router.post("/movies", tags = ["movies"] , response_model= dict, status_code =201 )
def create_movie(movie: Movie) -> dict:
    db = Session() #creando la sesion para acceder a la base de datos
    MovieService(db).create_movie(movie) #pasamos los datos como parametros con ** y convertimos movie a dict
    return JSONResponse(status_code =201, content= {"message": "pelicula registrada satisfactoriamente"})


#Usando PUT y DELETE

#put / actualizacion reemplazando datos existentes
@movie_router.put("/movies/{id}", tags = ["movies"], response_model= dict, status_code =200, responses={404: {"model": Message}} )
def replace_movie(id: int, movie: Movie)-> dict:
    
    #haciendo update para la base de datos
    db = Session()
    #verificamos que la pelicula a actualizar exista 
    result= MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code =404, content= {"message": "pelicula no encontrada"})
    
    # si enceuntra el id de la pelicula a modificar
    MovieService(db).update_movie(id, movie)
    
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})

    
    
    #################################################
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["catergory"] = movie.category
            return JSONResponse(status_code =200, content= {"message": "pelicula modificada satisfactoriamente"})
        else:
            return JSONResponse(status_code =404, content= {"message": "id no encontado"})

#delete
@movie_router.delete("/movies/{id}", tags = ["movies"], response_model= dict , status_code =200, responses={404: {"model": Message}})
def delete_movie(id: int)-> dict:
    
    db = Session()

    result= MovieService(db).get_movie(id)
    
    if not result:
        return JSONResponse(status_code=404 , content={"message": "Película no encontrada"})
    
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Película eliminada satisfactoriamente"})
    
    ######################################################
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(status_code =200, content= {"message": "pelicula eliminada satisfactoriamente"})
        else:
            return JSONResponse(status_code =404, content= {"message": "id no encontado"})