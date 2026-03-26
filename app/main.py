from fastapi import FastAPI, Depends
from app.database import engine, Base
from app.models import user
from app.routes import auth
from app.core.deps import get_current_user
from app.routes import task

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(task.router, prefix="/api", tags=["Task"])

# @app.get("/")
# def home():
#     return {"message": "API is working"}

@app.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"message": "You are authorized", "user": user}
