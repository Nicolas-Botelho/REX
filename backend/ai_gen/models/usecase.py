from typing import List
from pydantic import BaseModel, Field
from enum import Enum

from ai_gen.models.klass import Class, ClassAttributePrim, ClassAttributeEnum

class Step(BaseModel):
  id : int
  description : str

class Action(Step):
  next_step : int | None

class Decision(Step):
  next_steps : List[int] = Field(default_factory=list)

class ModificationTypeEnum(str, Enum):
  CREATE = "create"
  UPDATE = "update"
  DELETE = "delete"

class ModifyAction(Action):
  related_classes : List[Class] = Field(default_factory=list)
  action_type : ModificationTypeEnum

class ReadAction(Action):
  related_classes : List[Class] = Field(default_factory=list)
  read_attributes : List[ClassAttributePrim | ClassAttributeEnum] = Field(default_factory=list)

class TextReadAction(ReadAction):
  match_percent : float

class Actor(BaseModel):
  id : int
  name : str
  description : str

class Event(BaseModel):
  id : int
  name : str
  first_step : Action | Decision | ModifyAction | ReadAction | TextReadAction
  actor : Actor

class Usecase(BaseModel):
  id : int
  name : str
  usecase_events : List[Event] = Field(default_factory=list)