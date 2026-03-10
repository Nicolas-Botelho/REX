from typing import List
from pydantic import BaseModel

class Actor(BaseModel):
  iD : int
  name : str
  description : str | None

class Event(BaseModel):
  iD : int
  name : str
  actor : int
  usecase : int

class Step(BaseModel):
  iD : int
  system : bool
  description : str
  event : int

class Usecase(BaseModel):
  iD : int
  name : str