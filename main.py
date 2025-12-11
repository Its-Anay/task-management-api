from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
tasks = []

class task(BaseModel):
    task_id : int
    title : str
    description : Optional[str]

@app.get("/")
def root():
    return {"message": "Task API is running"}

@app.post("/tasks")
def add_tasks(title: str, description: str):
    task = { "task_id" :len(tasks) +1, "title": title, "description": description}
    tasks.append(task)
    return task
    
@app.get("/tasks")
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}")
def update_task(task_id: int,title: str,description: Optional[str] = None):
    for task in tasks:
        if task["task_id"] == task_id:
            task["title"] = title
            if description is not None:
                task["description"] = description            
            return task
    return{"error while updating"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for i,task in enumerate(tasks):
        if task["task_id"] == task_id:
            tasks.pop(i)
            return (f"task id:{task_id} removed succesfully")
    return{"error while deleting"}            