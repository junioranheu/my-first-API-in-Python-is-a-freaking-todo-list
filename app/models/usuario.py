from sqlalchemy.orm import Mapped, mapped_column, relationship # <-- Importe relationship
from sqlalchemy import String
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    senha_hash: Mapped[str] = mapped_column(String(255))

    # Navegação: Uma lista de tarefas vinculadas a este usuário
    tarefas: Mapped[list["Tarefa"]] = relationship(back_populates="criador")