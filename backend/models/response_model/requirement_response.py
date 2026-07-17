from models.requirement import Requirement
from models.question import Question

from pydantic import BaseModel, Field

class RequirementOutput(BaseModel):
  requirements: list[Requirement] = Field(default_factory=list)
  questions: list[Question] = Field(default_factory=list)