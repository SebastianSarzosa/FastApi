from typing import Union
from fastapi import FastAPI

#Creacion de una aplicacion FasTAPI:

app = FastAPI()


@app.get('/')
def read_root():
    return {'Nombre':'Sebastian  '}


@app.get('/hola')
def Hola_mundo():
    return {'Hola mundo'}


@app.get('/items/{item_id}')
def read_item(item_id : int, q: Union[str, None] = None):
    return{ 'item_id' : item_id, 'q' : q}


@app.get('/calculadora')
def calcular(operando_1: float,operando_2:float):
    return {'La suma de los dos numeros es' : operando_1+operando_2}







