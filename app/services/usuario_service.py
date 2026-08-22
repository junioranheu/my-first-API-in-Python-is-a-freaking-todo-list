from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.security import gerar_hash_senha
from fastapi import HTTPException

class UsuarioService:
    @staticmethod
    def criar(db: Session, usuario_dto: UsuarioCreate):
        usuario_existente = db.query(Usuario).filter(Usuario.email == usuario_dto.email).first()
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Email já cadastrado")

        novo_usuario = Usuario(
            email=usuario_dto.email,
            senha_hash=gerar_hash_senha(usuario_dto.senha)
        )
        
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        return novo_usuario