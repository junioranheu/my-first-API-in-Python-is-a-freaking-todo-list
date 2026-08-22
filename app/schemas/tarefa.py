from pydantic import BaseModel, ConfigDict, Field

# Classe base com propriedades comuns
class TarefaBase(BaseModel):
    # O Field adiciona Data Annotations de validação
    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str | None = None

# DTO de Entrada (Payload do POST)
class TarefaCreate(TarefaBase):
    pass

# DTO de Saída (Resposta da API)
class TarefaResponse(TarefaBase):
    id: int
    concluida: bool

    # Habilita a conversão de Model (SQLAlchemy) para Schema (Pydantic)
    model_config = ConfigDict(from_attributes=True)