from fastapi import FastAPI, Request
from app.routers import tarefa_router
from app.database import engine, Base  # <-- Base vem direto do database
from app.models.tarefa import Tarefa   # <-- Importamos para a Tarefa assinar a lista
from app.models.usuario import Usuario # <-- Importamos para o Usuario assinar a lista
from app.routers import usuario_router
from app.routers import auth_router
from fastapi.responses import JSONResponse

app = FastAPI(title="TO DO list - minha primeira API em Python com FastAPI", version="1.0.0")

# Captura qualquer exceção não tratada na aplicação
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": "erro",
            "description": "Erro interno no servidor",
            "details": str(exc) 
        }
    )

# Cria as tabelas no banco de dados (Equivalente ao EnsureCreated)
Base.metadata.create_all(bind=engine)

# Equivalente ao app.MapControllers()
app.include_router(tarefa_router.router) 
app.include_router(usuario_router.router)
app.include_router(auth_router.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}