from models.klass import Class, Inheritance, Association as HumanAssociation
from models.ai_klass import Association
from models.question import ClassQuestion

from pydantic import BaseModel, Field

class ClassOutput(BaseModel):
  classes: list[Class] = Field(default_factory=list)
  associations: list[Association] = Field(default_factory=list)
  inheritances: list[Inheritance] = Field(default_factory=list)
  questions: list[ClassQuestion] = Field(default_factory=list)

class HumanClassOutput(BaseModel):
  classes: list[Class] = Field(default_factory=list)
  associations: list[HumanAssociation] = Field(default_factory=list)
  inheritances: list[Inheritance] = Field(default_factory=list)
  questions: list[ClassQuestion] = Field(default_factory=list)