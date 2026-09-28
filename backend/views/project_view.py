# from generation.json_reader import JsonReader
from generation.json_project import JsonProject
from models.project import Project, ProjectView
from fastapi import APIRouter

import os
import uuid
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
  
  PROJECT_DIR = os.environ.get("PROJECT_DIR")

  project_dict = project.dict()

  def create_project_with_unique_name():
    while True:
      unique_name = uuid.uuid4().hex
      filepath = os.path.join(PROJECT_DIR, f"{unique_name}.json")
      try:
        open(filepath, "x").close()
        return filepath
      except FileExistsError:
        continue

  project_dict["filepath"] = create_project_with_unique_name()

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

  project = data.get("projects").pop(project_id)
  filepath = project.get("filepath")

  if os.path.exists(filepath):
    os.remove(filepath)

  jp.write_project(data)