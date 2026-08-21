from pydantic import BaseModel, Field
from enum import Enum

class Question(BaseModel):
  question: str

class NarrativeQuestion(Question):
  pass

class RequirementQuestion(Question):
  requirement_codes: list[str] = Field(default_factory=list)

class UsecaseQuestion(Question):
  usecase_names: list[str] = Field(default_factory=list)

class ClassQuestion(Question):
  class_names: list[str] = Field(default_factory=list)