from main import app #importa donde se ecuentra el archi principal
from fastapi.testclient import TestClient #importa el TestClient con el cual se puede relizar cualquier tipo de test
import requests#combinado con el json para trabajar asincronos 
import json#importa ek json para poder realizar un request con json
clientes = TestClient(app)
######################################################
def test_index():
    response = clientes.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Fast API"}
    
######################################################



def test_add():
    parametrosAdd = {"nombre":"name","email":"ejemplo@email.com","numero":"7752225588"}
    response = clientes.post("/clientes/", params=parametrosAdd)
    data_add = {"message":"usuario agregado"}
    assert response.status_code == 200
    assert response.json() == data_add
######################################################


def test_delete():
    response = clientes.delete("/clientes/3")
    dataCliente_delete = {"message":"usuario borrado"}
    assert response.status_code == 200
    assert response.json() == dataCliente_delete

    ##################################################