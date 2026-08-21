from models.requirement import FunctionalRequirement, NonFunctionalRequirement, BusinessRule, Actor
from models.question import RequirementQuestion

from pydantic import BaseModel, Field

class RequirementOutput(BaseModel):
  functional_requirements: list[FunctionalRequirement] = Field(default_factory=list)
  non_functional_requirements: list[NonFunctionalRequirement] = Field(default_factory=list)
  business_rules: list[BusinessRule] = Field(default_factory=list)
  questions: list[RequirementQuestion] = Field(default_factory=list)
  actors: list[Actor] = Field(default_factory=list)