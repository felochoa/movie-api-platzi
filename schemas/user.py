
from pydantic import BaseModel #para validar datos field

#clase para validación de usuario
class User(BaseModel):
    email: str
    password: str