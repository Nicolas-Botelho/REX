from pydantic import BaseModel, Field
from enum import Enum

from models.klass import Class, ClassAttribute

class Step(BaseModel):
  step_code : str
  description : str
  class_name: str

class Action(Step):
  next_step : str | None
  category: str

class Decision(Step):
  next_steps : list[str] = Field(default_factory=list)

class Actor(BaseModel):
  name : str
  description : str | None

class Event(BaseModel):
  name : str
  # description : str
  # first_step_code : str #| ModifyAction | ReadAction | TextReadAction
  event_steps : list[Action | Decision] = Field(default_factory=list)
  actor : Actor

class Usecase(BaseModel):
  name : str
  usecase_events : list[Event] = Field(default_factory=list)