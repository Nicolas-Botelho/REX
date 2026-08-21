from pydantic import BaseModel, Field
from enum import Enum

from models.requirement import Actor, FunctionalRequirement
from models.klass import Class, ClassAttribute

class CategoryEnum(str, Enum):
  INPUT = 'input'
  OUTPUT = 'output'
  VALIDATION = 'validation'
  CREATE = 'create'
  READ = 'read'
  UPDATE = 'update'
  DELETE = 'delete'
  INTEGRATION = 'integration'
  SUCCESS = 'success'
  FAILURE = 'failure'
  CANCEL = 'cancel'

class Step(BaseModel):
  step_code : str
  description : str
  class_name: str | None

# A step is associated with zero or one class. If a step would be associated with more than one class, it must be split into different steps

class Action(Step):
  next_step : str | None
  category: CategoryEnum

class Decision(Step):
  next_steps : list[str] = Field(default_factory=list)

class Event(BaseModel):
  name : str
  functional_requirements_codes : list[str]
  event_steps : list[Action | Decision] = Field(default_factory=list)
  actor_name : list[str] = Field(default_factory=list)

class Usecase(BaseModel):
  name : str
  usecase_events : list[Event] = Field(default_factory=list)