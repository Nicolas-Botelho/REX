from ai_gen.models.usecase import Usecase, Action, Decision, ModifyAction, ReadAction, TextReadAction

from typing import List
from pydantic import BaseModel, Field

class UsecaseOutput(BaseModel):
  usecases : List[Usecase] = Field(default_factory=list)
  event_steps : List[Action | Decision | ModifyAction | ReadAction | TextReadAction] = Field(default_factory=list)