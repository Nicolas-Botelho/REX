from ai_gen.models.requirements import FunctionalRequirement, NonFunctionalRequirement, BusinessRule

from typing import List
from pydantic import BaseModel

class FROutput(BaseModel):
  fr_list : List[FunctionalRequirement]

class NFROutput(BaseModel):
  nfr_list : List[NonFunctionalRequirement]

class BROutput(BaseModel):
  br_list : List[BusinessRule]