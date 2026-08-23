from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tarefa import TarefaResponse, TarefaCreate
from app.services.tarefa_service import TarefaService
from app.security import obter_usuario_logado

# Equivalente ao [Route("api/tarefas")]
router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

# GET: response_model garante que a saída siga o formato do DTO
@router.get("/", response_model=list[TarefaResponse])
def listar_tarefas(
    db: Session = Depends(get_db),
    usuario_id: int = Depends(obter_usuario_logado) # <-- Authorize
):
    return TarefaService.listar_todas(db)

# POST: Retorna 201 Created em caso de sucesso
@router.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefa(
    tarefa: TarefaCreate, 
    db: Session = Depends(get_db), 
    usuario_id: int = Depends(obter_usuario_logado) # <-- Authorize
):
    return TarefaService.criar(db, tarefa)

@router.put("/{tarefa_id}", response_model=TarefaResponse)
def atualizar_tarefa(
    tarefa_id: int, 
    tarefa: TarefaCreate, 
    db: Session = Depends(get_db),
    usuario_id: int = Depends(obter_usuario_logado) # <-- Authorize
):
    tarefa_atualizada = TarefaService.atualizar(db, tarefa_id, tarefa)
    
    if not tarefa_atualizada:
        # Equivalente ao return NotFound();
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return tarefa_atualizada

@router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(
    tarefa_id: int, 
    db: Session = Depends(get_db),
    usuario_id: int = Depends(obter_usuario_logado) # <-- Authorize   
):
    sucesso = TarefaService.deletar(db, tarefa_id)
    
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return # Retorna 204 sem corpo