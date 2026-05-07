from fastapi import FastAPI

from app.core.config import settings

from app.api.routes.context_routes import router as context_router

from app.db.init_db import init_db
from app.api.routes.db_test_routes import router as db_test_router
from app.api.routes.orchestrator_routes import router as orchestrator_router


app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(context_router)
app.include_router(db_test_router)
app.include_router(orchestrator_router)


@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/")
async def root():
    return {
        "message": "LLM Orchestrator System Running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }