from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from urllib import response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

import pyrebase
import hashlib


class User(BaseModel):
    email: str
    password: str

class response(BaseModel):
    message: str

app = FastAPI()
origins = [
    "*",    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)


@app.get("/")
async def root():
    return {"message": "hello wordXD"}

firebaseConfig = {
    "apiKey": "AIzaSyCEkkxRet_lOOvEY4Joq22udSyrHI7gOa0",
    "authDomain": "fb-api-29ea3.firebaseapp.com",
    "databaseURL": "https://fb-api-29ea3-default-rtdb.firebaseio.com",
    "projectId": "fb-api-29ea3",
    "storageBucket": "fb-api-29ea3.appspot.com",
    "messagingSenderId": "500610176971",
    "appId": "1:500610176971:web:187e97d09e0a786a4a484e"
}

firebase = pyrebase.initialize_app(firebaseConfig)


SecurityBasic = HTTPBasic()
SecurityBearer = HTTPBearer()



@app.get(
    "/users/token/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Get a token for user ",
    description="Get a token for user ",
    tags=["auth"]
)
async def get_token(credentials: HTTPBasicCredentials = Depends(SecurityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)

        response = {
            "token": user['idToken'],
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.get(
    "/users/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Get a user",
    description="Get a user",
    tags=["auth"]
)
async def get_user(credentials: HTTPAuthorizationCredentials = Depends(SecurityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId']

        db = firebase.database()
        user_data = db.child("users").child(uid).get().val()

        response = {
            "user_data": user_data
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

####################################################################################################################


@app.post(
    "/users/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Agregar Usuario",
    description="Agregar Usuario",
    tags=["add"]
)
async def add_user(add_post: User):
    try:
        email = add_post.email
        password = add_post.password
        auth = firebase.auth()
        datos = {
            'email':email, 
            'nivel': '1',
            'nombre': 'user'
        }
        dato = auth.create_user_with_email_and_password(email, password)
        db=firebase.database()
        db.child("users").child(dato["localId"]).set (datos)
        return {"message":"usuario agregado"} 

    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

