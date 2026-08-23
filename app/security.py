import os
from datetime import datetime, timedelta, timezone
import jwt
import bcrypt 

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Avisa o FastAPI onde o cliente deve ir para obter o token (aponta para nossa rota /token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

def obter_usuario_logado(token: str = Depends(oauth2_scheme)):
    excecao_credenciais = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica o token JWT usando nossa chave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id: str = payload.get("sub")
        if usuario_id is None:
            raise excecao_credenciais
    except InvalidTokenError:
        raise excecao_credenciais
        
    return int(usuario_id)