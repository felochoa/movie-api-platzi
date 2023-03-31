from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token #creación de tokens con jwt
from schemas.user import User

#creacion del router
auth_router = APIRouter()


#metodo de autentificación de usuario
@auth_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code= 200, content =token)
    return user