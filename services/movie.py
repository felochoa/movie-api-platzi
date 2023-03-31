
from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService(): 
    #cada vez que se use este servicio se envie una sesion a la base de datos
    def __init__(self, db) -> None: 
    
    #ya puedo tener acceso a la base de datps para que pueda ser accesible a otros metodos de este servicio
        self.db = db 

    #metodo 1 - get movies
    def get_movies(self):
        result = self.db.query(MovieModel).all()    
        return result
    
    #metodo 2 - get movies by id
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()    
        return result
    
    #metodo 3 - get movies by categoria
    def get_movie_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    #metodo 4 - añadiendo datos de peliculas
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict()) #pedimos todos los datos de la clase Movie
        self.db.add(new_movie)
        self.db.commit()
        return
    
    #metodo 5- modificando datos de peliculas
    def update_movie(self, id: int, data: Movie): #para modificar se necesita el id de la peli a modificar y los datos del objeto tipo movie
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        
        movie.title= data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return 

    #metodo 6 - eliminando peliculas
    def delete_movie(self, id: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(movie)
        self.db.commit()
        return