from fastapi import FastAPI, Depends
from app.database import engine, Base
from app.models import user
from app.routes import auth
from app.core.deps import get_current_user
from app.routes import task
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

# @app.get("/")
# def home():
#     return {"message": "API is working"}


@app.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"message": "You are authorized", "user": user}
