from pydantic import BaseModel

class Project(BaseModel):
  name: str
  description: str
  filepath: str

class ProjectView(BaseModel):
  name: str
  description: str