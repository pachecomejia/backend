#import secrets
#import hashlib  # importa la libreria hashlib
#import os
#import sqlite3
#from fastapi.middleware.cors import CORSMiddleware
#from typing import List
#from fastapi import Depends, FastAPI, HTTPException, status
#from fastapi.security import HTTPBasic, HTTPBasicCredentials
#from pydantic import BaseModel 
#app = FastAPI()

#from typing import Union

#from typing import List

#from pydantic import BaseModel

#DATABASE_URL = os.path.join("clientes.sqlite")#base de datos a llamar 

#class response(BaseModel): #define la clase 1
#    message: str


    #muestra los reguistros
#class Cliente(BaseModel):#define la clase de clientes actualizados 
#    id_cliente: int
#    nombre: str
#    email: str
#    numero: int



    
#######################################################################################3
#DATABASE_URL = os.path.join("clientes.sqlite")#base de datos a llamar 
#from fastapi.middleware.cors import CORSMiddleware

    
#app = FastAPI()

#security = HTTPBasic()
#origins = [
#    "*",
#    "*",
#]

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins = origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"]
    

#)

#######################################################################################

#def index(credentials: HTTPBasicCredentials = Depends(security)):
#    password_b = hashlib.md5(credentials.password.encode())
#    password = password_b.hexdigest()
#    with sqlite3.connect(DATABASE_URL) as connection:
#        cursor = connection.cursor()
##        cursor.execute(
#            "SELECT level FROM usuarios WHERE username = ? and password = ?",
#            (credentials.username, password),
#        )
#        user = cursor.fetchone()
#        if not user:
#            raise HTTPException(
#                status_code=status.HTTP_401_UNAUTHORIZED,
#                detail="Incorrect username or password",
#               headers={"WWW-Authenticate": "Basic"},
#          )
#    return user[0]
#    return admin[1]


####################################################################################
#Solo regresa el mensaje de fastapi

#@app.get("/", response_model=response)#url donde se puede buscar 
#async def index(level: int = Depends(index)):
#    return {"message": "Fast API"}#mensaje de correcta ejecucion
    


#regresa a todos los usuarios agregados a la base de datos 
#@app.get("/clientes/", response_model=List[Cliente])
#async def getProductos():
#    with sqlite3.connect('clientes.sqlite') as connection:
#        connection.row_factory = sqlite3.Row
#        cursor = connection.cursor()
#        cursor.execute('SELECT * FROM clientes')
#        response = cursor.fetchall()
#        return response
#    