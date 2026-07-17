from pydantic import BaseModel, Field
from enum import Enum

class User(BaseModel):
  name: str
  description: str

class DomainNarrative(BaseModel):
  system_context: str
  users: list[User] = Field(default_factory=list)
  system_functionalities: list[str] = Field(default_factory=list)

class RequirementEnum(str, Enum):
  FUNCTIONAL_REQUIREMENT = "functional_requirement"
  NON_FUNCTIONAL_REQUIREMENT = "non_functional_requirement"
  BUSINESS_RULE = "business_rule"

class Requirement(BaseModel):
  code: str
  description: str
  requirement_type: RequirementEnum
  depends_on_requirements_codes: list[str] = Field(default_factory=list)