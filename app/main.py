from fastapi import FastAPI

from app.core.config import settings

from app.api.routes.context_routes import router as context_router


app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(context_router)


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