from fastapi import FastAPI
from app.routers import tarefa_router
from app.database import engine, Base  # <-- Base vem direto do database
from app.models.tarefa import Tarefa   # <-- Importamos para a Tarefa assinar a lista
from app.models.usuario import Usuario # <-- Importamos para o Usuario assinar a lista
from app.routers import usuario_router
from app.routers import auth_router

app = FastAPI(title="TO DO list - minha primeira API em Python com FastAPI", version="1.0.0")

# Cria as tabelas no banco de dados (Equivalente ao EnsureCreated)
Base.metadata.create_all(bind=engine)

# Equivalente ao app.MapControllers()
app.include_router(tarefa_router.router) 
app.include_router(usuario_router.router)
app.include_router(auth_router.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}