from sqlalchemy.orm import Session
from app.models.tarefa import Tarefa
from app.schemas.tarefa import TarefaCreate

class TarefaService:
    @staticmethod
    def listar_todas(db: Session):
        # Equivalente ao _context.Tarefas.ToList()
        return db.query(Tarefa).all()

    @staticmethod
    def criar(db: Session, tarefa_dto: TarefaCreate):
        # Transforma o DTO em Entidade (o ** desempacota o dicionário)
        nova_tarefa = Tarefa(**tarefa_dto.model_dump()) 
        
        db.add(nova_tarefa)
        db.commit()          # Equivalente ao _context.SaveChanges()
        db.refresh(nova_tarefa) # Recarrega para pegar o ID gerado pelo banco
        return nova_tarefa