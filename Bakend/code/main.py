import secrets
import hashlib  # importa la libreria hashlib
import os
import sqlite3
from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel 
from typing import Union
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


######################################################
DATABASE_URL = os.path.join("clientes.sqlite")#base de datos a llamar 

class clientes(BaseModel):
    username: str
    level: int
class response(BaseModel): #define la clase 
    message: str

class Cliente(BaseModel):#define una clase 
    id_cliente: int
    nombre: str
    email: str
    numero: str
class cliente_add(BaseModel):
    nombre: str
    email: str
    numero: int
##################################################################################
    


app = FastAPI()

security = HTTPBasic()




#######################################################################################3
DATABASE_URL = os.path.join("clientes.sqlite")#base de datos a llamar 
app = FastAPI()
security = HTTPBasic()
class Usuarios(BaseModel):
    username: str
    level: int
security = HTTPBasic()
origins = [
    "https://8080-pachecomejia-backend-0lv4cfaix24.ws-us51.gitpod.io",    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)


#######################################################################################3


def index(credentials: HTTPBasicCredentials = Depends(security)):
    password_b = hashlib.md5(credentials.password.encode())
    password = password_b.hexdigest()
    with sqlite3.connect(DATABASE_URL) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT level FROM usuarios WHERE username = ? and password = ?",
            (credentials.username, password),
        )
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    return user[0]#return credentials.username

@app.get("/", response_model=response)#url donde se puede buscar 
async def index(username: str = Depends(index)):
    return {"message": "Fast API"}#mensaje de correcta ejecucion 
    
@app.get("/clientes/")
async def clientes(offset:int =0,limit: int = 10,level: int = Depends(index)):
    data = {limit,offset}
    return data
    

    
#################################################################################################################
#regresa a todos los usuarios agregados a la base de datos 
@app.get("/user/", response_model=List[Cliente])
async def get_clientes(level: int = Depends(index)):
    with sqlite3.connect('clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchall()
        return response
    

@app.post("/cliente/", response_model=response)#url donde se puede buscar con el post /docs 
async def cliente_add(nombre:str,email:str,numero:str, level: int = Depends(index)): #definicion de campos que pueden añadir 
    with sqlite3.connect("clientes.sqlite") as connection: #creacion  de donde se conectara y dopnde se ecuentra la base de datos creada 
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("insert into clientes(nombre,email,numero) values ('{nombre}', '{email}','{numero}')".format(nombre=nombre, email=email, numero=numero)) #campos que incluira la base de datos creada esto para poder relizar una comparacion con la que se ecnuentra en el archivo clientes.sql 
        response = cursor.fetchone()
        data = {"message":"usuario agregado"}#mensaje de la correcta ejecucion del post al añadir algun cambio 
        return data

@app.put("/clientes/{id_usuario}", response_model=response)#url donde se puede buscar con el put /docs 
async def cliente_put(id_cliente: int, nombre: str,email:str,level: int = Depends(index)): #en esta parte define los campos que deberia lleavar para poder modificar 
    with sqlite3.connect("clientes.sqlite") as connection:#creacion de la conectividad y la ruta donde se encunetra el archivo de ejecucion
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("Update clientes set nombre = '{name}', email = '{email}' where id_cliente = {id}".format(name=nombre,email=email,id=id_cliente))#campos que debe incluir el campo donde se de sea ejecutar
        response = cursor.fetchone()
        data = {"message":"usuario actualizado"}#mensaje de una correcta ejecucion 
        return data

@app.delete("/clientes/{id_cliente}", response_model=response)#crea una url donde se puede buscar dicho campo asi como los apartados que debe de llevar 
async def cliente_delete(id_cliente: int,level: int = Depends(index)):#muestra el campo adicional 
    with sqlite3.connect("clientes.sqlite") as connection:#conectividad con la carpeta en la que se debe alojar 
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("delete from clientes where id_cliente = {}".format(id_cliente))#campos que se pueden eliminar 
        response = cursor.fetchone()
        data = {"message":"usuario borrado"}#mensaje de que la ejhecucion del delete se ejecuto de manera correcta 
        return 