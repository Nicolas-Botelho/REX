from ai_gen.models.klass import Class, Inheritance
from ai_gen.models.ai_klass import Association

from typing import List
from pydantic import BaseModel, Field

class ClassOutput(BaseModel):
  classes: list[Class] = Field(default_factory=list)
  associations: list[Association] = Field(default_factory=list)
  inheritances: list[Inheritance] = Field(default_factory=list)