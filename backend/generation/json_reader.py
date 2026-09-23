import os
import json
from dotenv import load_dotenv

class JsonReader():
  def __init__(self, file_path: str):
    self.path = file_path

  def read(self) -> dict:
    if os.path.exists(self.path):
      with open(self.path, "r", encoding="utf-8") as f:
        return json.load(f)
    else:
      return {}
  
  def read_projects():
    load_dotenv()
    
    PROJECT_DIR = os.environ.get("PROJECT_DIR")

    if os.path.exists(PROJECT_DIR+"projects.json"):
      with open(PROJECT_DIR+"projects.json", "r", encoding="utf-8") as f:
        projects = json.load(f).get("projects")
      return projects
    else:
      return []