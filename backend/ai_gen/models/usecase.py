from typing import List
from pydantic import BaseModel

class Actor(BaseModel):
  semantic_id : str
  name : str
  description : str | None

class Event(BaseModel):
  semantic_id : str
  name : str
  actor : str
  usecase : str

class Step(BaseModel):
  semantic_id : str
  system : bool
  description : str
  event : str

class Usecase(BaseModel):
  semantic_id : str
  name : str