from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, user

Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Roaster Backend")
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
