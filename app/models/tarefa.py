from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from app.database import Base

# Equivalente a uma classe de Entidade no EF Core
class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str | None] = mapped_column(String(255), nullable=True)
    concluida: Mapped[bool] = mapped_column(Boolean, default=False)