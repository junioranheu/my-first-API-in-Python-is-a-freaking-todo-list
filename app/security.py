import os
from datetime import datetime, timedelta, timezone
import jwt
import bcrypt 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def gerar_hash_senha(senha: str) -> str:
    # bcrypt exige bytes, então codificamos a string
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    
    # Decodificamos de volta para string para salvar no PostgreSQL
    return senha_hash.decode('utf-8') 

def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    # Compara a senha digitada (em bytes) com o hash do banco (em bytes)
    return bcrypt.checkpw(senha_plana.encode('utf-8'), senha_hash.encode('utf-8'))

def criar_token_acesso(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt