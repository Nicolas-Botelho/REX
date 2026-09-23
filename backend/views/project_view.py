# from generation.json_reader import JsonReader
from generation.json_project import JsonProject
from models.project import Project, ProjectView
from fastapi import APIRouter

import os
from dotenv import load_dotenv

project_router = APIRouter(prefix="/project")

@project_router.get("/project/")
def get_projects():
  jp = JsonProject()
  data = jp.return_projects(view=True)

  return {"data": data}

@project_router.get("/project/{project_id}/")
def get_project(project_id: int):
  jp = JsonProject()
  data = jp.return_projects(view=True)

  if len(data.get("projects")) > project_id:
    return {"data": data.get("projects")[project_id]}
  return {"data": None}

@project_router.post("/project/")
def create_project(project: ProjectView):
  jp = JsonProject()
  data = jp.return_projects()
  load_dotenv()
  
  PROJECT_DIR = os.environ.get("PROJECT_DIR")

  project_dict = project.dict()
  project_dict["filepath"] = PROJECT_DIR+f"{project.name}.json"

  data.get("projects").append(project_dict)
  jp.write_project(data)

@project_router.put("/project/{project_id}/")
def update_project(project_id: int, project: ProjectView):
  jp = JsonProject()
  data = jp.return_projects()

  filepath = data.get("projects")[project_id].get("filepath")
  
  data.get("projects")[project_id] = Project(name=project.name, description=project.description, filepath=filepath)
  jp.write_project(data)

@project_router.delete("/project/{project_id}/")
def delete_project(project_id: int):
  jp = JsonProject()
  data = jp.return_projects()

  data.get("projects").pop(project_id)
  jp.write_project(data)