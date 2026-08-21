from pydantic import BaseModel, Field
from enum import Enum

####################
# DOMAIN NARRATIVE #
####################

class DomainNarrative(BaseModel):
  narrative: str

################
# REQUIREMENTS #
################

class PriorityEnum(str, Enum):
  MUST = 'must'
  SHOULD = 'should'
  COULD = 'could'
  WONT = 'wont'

class NFRCategoryEnum(str, Enum):
  RELIABILITY = 'reliability'
  USABILITY = 'usability'
  PERFORMANCE = 'performance'
  SECURITY = 'security'
  COMPATIBILITY = 'compatibility'
  MAINTAINABILITY = 'maintainability'
  FLEXIBILITY = 'flexibility'

class Actor(BaseModel):
  name: str
  description: str

class Requirement(BaseModel):
  code: str
  description: str

class FunctionalRequirement(Requirement):
  actor_name: str
  objective: str
  depends_on_requirements_codes: list[str]
  apply_business_rules_codes: list[str]
  priority: PriorityEnum

class NonFunctionalRequirement(Requirement):
  category: NFRCategoryEnum
  applies_on_requirements_codes: list[str]
  priority: PriorityEnum

class BusinessRule(Requirement):
  pass