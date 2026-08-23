from sqlalchemy.orm import Session
from app.models.tarefa import Tarefa
from app.schemas.tarefa import TarefaCreate

class TarefaService:
    @staticmethod
    def listar_todas(db: Session):
        # Equivalente ao _context.Tarefas.ToList()
        return db.query(Tarefa).all()

    @staticmethod
    def criar(db: Session, tarefa_dto: TarefaCreate, usuario_id: int):
        # Passamos os dados do DTO e adicionamos o usuario_id explicitamente
        nova_tarefa = Tarefa(**tarefa_dto.model_dump(), usuario_id=usuario_id) 
        
        db.add(nova_tarefa)
        db.commit()          # Equivalente ao _context.SaveChanges()
        db.refresh(nova_tarefa) # Recarrega para pegar o ID gerado pelo banco
        return nova_tarefa

    @staticmethod
    def buscar_por_id(db: Session, tarefa_id: int):
        # Equivalente ao _context.Tarefas.FirstOrDefault(t => t.Id == id)
        return db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    @staticmethod
    def atualizar(db: Session, tarefa_id: int, tarefa_dto: TarefaCreate, usuario_id: int):
        tarefa = TarefaService.buscar_por_id(db, tarefa_id)

        if not tarefa:
            return None # Retornamos None para o Controller decidir o que fazer
        
        tarefa.titulo = tarefa_dto.titulo
        tarefa.descricao = tarefa_dto.descricao
        tarefa.usuario_id = usuario_id
        db.commit()
        db.refresh(tarefa)
        return tarefa

    @staticmethod
    def deletar(db: Session, tarefa_id: int):
        tarefa = TarefaService.buscar_por_id(db, tarefa_id)
        if not tarefa:
            return False
        
        db.delete(tarefa)
        db.commit()
        return True