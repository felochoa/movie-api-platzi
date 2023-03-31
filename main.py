from fastapi import FastAPI  #path: para validacion de parametros de ruta, query = validar parametros query
from fastapi.responses import HTMLResponse , JSONResponse
from pydantic import BaseModel #para validar datos field
from utils.jwt_manager import create_token #creación de tokens con jwt
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import auth_router

Base.metadata.create_all(bind = engine)

app = FastAPI() #instancia de fast api
app.title = "mi app con FastAPI" #podemos cambiar el titulo de http://localhost:5000/docs
app.version = "0.0.1" #cambiando la version - se ve el cambio en http://localhost:5000/docscambio en 

#añadiendo el middleware para hacer error handling

app.add_middleware(ErrorHandler) #le paso el middleware que es Errorhandler

#incluyendo el router de movies y el de autentificador de usuario- aqui se encuentran todos los metodos de movies
app.include_router(movie_router)

app.include_router(auth_router)


#clase para respuesta a errores 404 o otros ver https://fastapi.tiangolo.com/advanced/additional-responses/
class Message(BaseModel):
    message: str



# lista con diccionarios de las peliculas
movies = [
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 3,
        'title': 'Avatar 3',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }
    ] 

#pirmer endpoint
@app.get("/", tags=["home"]) #ruta de inicio , tags para modificar el default

def message():
    #retornando archivo HTML
    return HTMLResponse("<h1>hola</h1>")





