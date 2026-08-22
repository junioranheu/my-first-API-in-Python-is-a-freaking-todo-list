from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexão (SQLite local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./todolist.db"

# Engine de conexão com o banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fábrica de sessões (equivalente à injeção do DbContext)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para as nossas entidades
class Base(DeclarativeBase):
    pass