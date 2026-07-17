from typing import Annotated, TypedDict, Optional, List
from operator import add

from models.response_model.narrative_response import NarrativeOutput
from models.response_model.requirement_response import RequirementOutput
from models.response_model.usecase_response import UsecaseOutput
from models.response_model.class_response import ClassOutput

class State(TypedDict):
  InputText : str

  OldDomainNarrative : Optional[NarrativeOutput]
  OldRequirements : Optional[RequirementOutput]
  OldClasses : Optional[ClassOutput]
  OldUsecases : Optional[UsecaseOutput]

  DomainNarrative : Optional[NarrativeOutput]
  Requirements : Optional[RequirementOutput]
  Classes : Optional[ClassOutput]
  Usecases : Optional[UsecaseOutput]