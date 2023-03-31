
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_tokens #creación de tokens con jwt

#clase de midleware - solicitar token generador al usuario y validar
class JWTBearer(HTTPBearer): #hereda a HTTPBEarer
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data= validate_tokens(auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas" )