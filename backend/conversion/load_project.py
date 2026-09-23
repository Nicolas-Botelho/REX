from generation.json_reader import JsonReader
from models.project import ProjectView, Project

class ProjectLoader():
  def __init__(self, view=False):
    self.view = view

  def load(self):
    models = JsonReader.read_projects()

    return self.load_projects(models)
  
  def load_projects(self, models: list):
    if self.view:
      projects: list[ProjectView] = []
      try:
        for m in models:
          projects.append(ProjectView.model_validate(m))
      except Exception as e:
        print(f"INVALID PROJECT {e}: {model}")
    else:
      projects: list[Project] = []
      try:
        for m in models:
          projects.append(Project.model_validate(m))
      except Exception as e:
        print(f"INVALID PROJECT {e}: {model}")
    return projects