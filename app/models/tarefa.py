from sqlalchemy.orm import Mapped, mapped_column, relationship # <-- Importe relationship
from sqlalchemy import String, Boolean, ForeignKey             # <-- Importe ForeignKey
from app.database import Base

# Equivalente a uma classe de Entidade no EF Core
class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str | None] = mapped_column(String(255), nullable=True)
    concluida: Mapped[bool] = mapped_column(Boolean, default=False)

    # Chave estrangeira ligando à tabela de usuários
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    
    # Navegação (Não vira coluna no banco, é só para o Python)
    criador: Mapped["Usuario"] = relationship(back_populates="tarefas")