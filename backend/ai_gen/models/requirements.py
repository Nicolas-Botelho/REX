from typing import List
from pydantic import BaseModel

class Requirement(BaseModel):
  iD = int
  description = str

class FunctionalRequirement(Requirement):
  testCase = List[int]
  epics = List[int]

class NonFunctionalRequirement(Requirement):
  frs = List[int]

class BusinessRules(Requirement):
  frs = List[int]