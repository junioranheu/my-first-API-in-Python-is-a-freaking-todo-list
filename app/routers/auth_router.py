from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.security import verificar_senha, criar_token_acesso

router = APIRouter(tags=["Autenticação"])
 
# O endpoint padrão para gerar o token costuma ser /token
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # O form_data padrão do OAuth2 usa o campo 'username', então enviaremos o email por ele
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    
    # Valida se o usuário existe e se a senha bate com o hash
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Colocamos o ID do usuário dentro do token (no campo 'sub' - subject)
    token = criar_token_acesso(data={"sub": str(usuario.id)})
    
    # O FastAPI exige que o retorno tenha exatamente esta estrutura de dicionário
    return {"access_token": token, "token_type": "bearer"}