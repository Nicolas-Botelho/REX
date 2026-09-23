import json
import os
from dotenv import load_dotenv

from models.project import Project
from conversion.load_project import ProjectLoader

class JsonProject():
  def return_projects(self, view: bool = False):
    pl = ProjectLoader(view=view)
    projects_data = pl.load()

    data = {
      "projects": [p.dict() for p in projects_data]
    }
    return data

  def save_project(self, data: dict):
    # load_dotenv()
    
    PROJECT_DIR = os.environ.get("PROJECT_DIR")

    with open(PROJECT_DIR+"projects.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4, ensure_ascii=False)

  def write_project(self, data: dict):
    try:
      valid_data = {
        "projects": [Project.model_validate(p).dict() for p in data.get("projects")]
      }

      self.save_project(valid_data)
    except Exception as e:
      print(f"INVALID DATA {e}: {data}")