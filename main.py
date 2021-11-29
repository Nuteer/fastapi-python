from fastapi import FastAPI
import fastapi

from pydantic import BaseModel

app = fastapi()

#rota raiz
@app.get("/")
def raiz():
    return {"my fastapi": "apipython"}

#criar model
class Usuario(BaseModel):
    id: int
    email: str
    senha:str

#criar base de dados

base_de_dados = [
    Usuario(id=1; email="nuteer@nuteer.com.br", senha="senha123"),
    Usuario(id=2; email="teste@teste.com.br", senha="teste123")
]

# rota Get ALL
@app.get("/usuarios")
def get_todo_os_usuarios():
    return base_de_dados

# rota Get id
@app.get("/usuarios/{id_usuario: int}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados: