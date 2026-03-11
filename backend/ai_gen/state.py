from typing import Annotated, TypedDict, Optional, List
from operator import add

from ai_gen.models.response_model.usecase_response import UsecaseOutput
from ai_gen.models.response_model.class_response import ClassOutput

class State(TypedDict):
  InputText : str

  OldClasses : Optional[ClassOutput]
  OldUsecases : Optional[UsecaseOutput]

  Classes : Optional[ClassOutput]
  Usecases : Optional[UsecaseOutput]