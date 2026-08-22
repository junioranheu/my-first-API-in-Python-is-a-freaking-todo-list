from fastapi import FastAPI

# Equivalente ao builder.Build()
app = FastAPI(
    title="Minha API Python",
    description="API com FastAPI, SQLAlchemy e Pydantic"
)

# Equivalente a um [HttpGet("health")] no Controller
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API rodando perfeitamente!"}