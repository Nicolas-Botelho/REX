from ai_gen.models.klass import Enum, Class

from typing import List
from pydantic import BaseModel, Field

class ClassOutput(BaseModel):
  classes : List[Class] = Field(default_factory=list)