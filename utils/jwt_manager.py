from jwt import encode , decode

#funcion para crear tokes
def create_token(data: dict):
    #payload = contenido que voy a convertir a un token
    #key = clave del token
    # algorithm = algoritmo usado para generar el token
    token: str = encode(payload = data, key ="secret key", algorithm = "HS256" ) 
    return token

#validar tokens
def validate_tokens(token : str) -> dict:
    data: dict = decode(token, key="secret key", algorithms=["HS256"])
    return data