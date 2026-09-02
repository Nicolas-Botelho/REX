from pydantic import BaseModel, Field
from enum import Enum

from models.requirement import Actor, FunctionalRequirement
from models.klass import Class, ClassAttribute

class DataOperationEnum(str, Enum):
  VALIDATION = 'validation'
  CREATE = 'create'
  READ = 'read'
  UPDATE = 'update'
  DELETE = 'delete'

class ComplexOperationEnum(str, Enum):
  HTTP = 'http api call'
  SMTP = 'smtp api call'
  MATH = 'math'
  OTHER = 'other'

class NavOperationEnum(str, Enum):
  INCLUDE = 'include'
  MODAL = 'modal'
  NAVIGATE = 'navigate'

class IOOperationEnum(str, Enum):
  INPUT = 'input'
  OUTPUT = 'output'

class DataOperation(BaseModel):
  attributes: dict[str, list[str]] = Field(default_factory=dict, description="dict_key: class name; dict_value: list of the attributes and associations (a class name in the value)")
  operation_type: DataOperationEnum

class ComplexOperation(BaseModel):
  description: str
  operation_type: ComplexOperationEnum

class NavOperation(BaseModel):
  usecase_name: str
  event_name: str
  operation_type: NavOperationEnum

class IOOperation(BaseModel):
  description: str
  operation_type: IOOperationEnum

class Step(BaseModel):
  step_code : str
  description : str

class Action(Step):
  next_step : str | None
  category: DataOperation | ComplexOperation | NavOperation | IOOperation# | None

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