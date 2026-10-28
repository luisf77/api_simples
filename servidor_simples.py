from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pedido(BaseModel):
    nome: str

@app.post("/saudacao")
def saudacao(pedido: Pedido):
    msg = f"Olá, {pedido.nome}"
    return {"mensagem": msg}

class PedidoNumero (BaseModel):
    numero: float

@app.post("/dobro")
def dobro(pedido: PedidoNumero):
    return {"resultado": pedido.numero * 2}

