from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.tarefa import TarefaResponse, TarefaCreate
from app.services.tarefa_service import TarefaService

# Equivalente ao [Route("api/tarefas")]
router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

# GET: response_model garante que a saída siga o formato do DTO
@router.get("/", response_model=list[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return TarefaService.listar_todas(db)

# POST: Retorna 201 Created em caso de sucesso
@router.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    return TarefaService.criar(db, tarefa)