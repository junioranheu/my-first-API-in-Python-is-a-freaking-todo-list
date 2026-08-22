from fastapi import FastAPI
from app.routers import tarefa_router
from app.database import engine
from app.models.tarefa import Base 

app = FastAPI(title="TO DO list - minha primeira API em Python com FastAPI", version="1.0.0")

# Cria as tabelas no banco de dados (Equivalente ao EnsureCreated)
Base.metadata.create_all(bind=engine)

# Equivalente ao app.MapControllers()
app.include_router(tarefa_router.router) 

@app.get("/health")
def health_check():
    return {"status": "ok"}