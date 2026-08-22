from pydantic import BaseModel, ConfigDict, Field

class UsuarioCreate(BaseModel):
    email: str
    senha: str = Field(..., max_length=72) # Bloqueia senhas maiores que 72 caracteres

class UsuarioResponse(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)