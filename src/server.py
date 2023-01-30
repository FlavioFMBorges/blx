from fastapi import FastAPI

app = FastAPI()

@app.get('/produtos')
def listar_produto():
    return {'Msg': 'Listagem de Produtos'}