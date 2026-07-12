# Importando bibliotecas
from fastapi import FastAPI
from backend.app.routers.health import router as health_router

# Cria a aplicação
app = FastAPI(
    title='BI Assistant AI',
    version='1.0.0'
)

app.include_router(health_router)