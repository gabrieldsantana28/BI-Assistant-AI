# Importando bibliotecas
from fastapi import FastAPI

# Cria a aplicação
app = FastAPI()


@app.get('/')
def home():
    return {
        'message': 'Bem-vindo ao BI Assistant AI'
    }