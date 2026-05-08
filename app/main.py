from fastapi import FastAPI

from app.core.config import settings

from app.api.routes.context_routes import router as context_router

from app.db.init_db import init_db
from app.api.routes.db_test_routes import router as db_test_router
from app.api.routes.orchestrator_routes import router as orchestrator_router
from app.api.routes.rag_routes import router as rag_router

from app.api.routes.stream_routes import (
    router as stream_router
)

from app.api.routes.trace_routes import (
    router as trace_router
)

from app.api.routes.eval_routes import (
    router as eval_router
)

from app.api.routes.prompt_routes import (
    router as prompt_router
)


app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(context_router)
app.include_router(db_test_router)
app.include_router(orchestrator_router)
app.include_router(rag_router)
app.include_router(stream_router)
app.include_router(trace_router)
app.include_router(eval_router)
app.include_router(prompt_router)


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