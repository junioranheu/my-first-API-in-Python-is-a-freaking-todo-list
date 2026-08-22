import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

# Procura o arquivo .env e carrega as variáveis para a memória
load_dotenv()

# Busca a string de conexão de forma segura
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Fábrica de sessões (equivalente à injeção do DbContext)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para as nossas entidades
class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db # Entrega a sessão para o Controller usar
    finally:
        db.close() # Garante que a conexão será fechada