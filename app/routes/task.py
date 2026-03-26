from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate
from app.core.deps import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    
    new_task = Task(
        title=task.title,
        description=task.description,
        owner=user["sub"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task







@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    
    tasks = db.query(Task).filter(Task.owner == user["sub"]).all()
    
    return tasks

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):

    db_task = db.query(Task).filter(Task.id == task_id, Task.owner == user["sub"]).first()

    if not db_task:
        return {"error": "Task not found"}

    db_task.title = task.title
    db_task.description = task.description

    db.commit()
    db.refresh(db_task)

    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):

    db_task = db.query(Task).filter(Task.id == task_id, Task.owner == user["sub"]).first()

    if not db_task:
        return {"error": "Task not found"}

    db.delete(db_task)
    db.commit()

    return {"message": "Task deleted"}