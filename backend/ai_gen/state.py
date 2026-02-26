from typing import Annotated, TypedDict, Optional, List
from operator import add

class State(TypedDict):
  InputText : str

  OldBusinessRules : Optional[List]
  OldNonFunctionalRequirements : Optional[List]
  OldFunctionalRequirements : Optional[List]

  BusinessRules : Optional[List]
  NonFunctionalRequirements : Optional[List]
  FunctionalRequirements : Optional[List]