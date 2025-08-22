from fastapi import FastAPI
from app.api import auth, users, ai, admin

app = FastAPI(
    title="Sekai AI Platform",
    description="A futuristic, customizable AI chat platform.",
    version="0.1.0"
)

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(ai.router, prefix="/ai")
app.include_router(admin.router, prefix="/admin")