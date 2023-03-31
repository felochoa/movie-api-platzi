from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    
    #metodo que estará dectectando si hay un error en mi aplicación

    # call next
    #response - se envia en caso de que no ocurra un error 
    #si ocurre un error devuelve response o JSONresponse

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse: 
        
        try:
            return await call_next(request)
        except Exception as e:
            # se debe retornar el error convertido a string
            return JSONResponse(status_code=500, content={"error": str(e) })