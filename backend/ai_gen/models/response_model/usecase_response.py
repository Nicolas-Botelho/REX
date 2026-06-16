from ai_gen.models import usecase as uc_mod

from typing import List
from pydantic import BaseModel, Field

class UsecaseOutput(BaseModel):
  usecases : List[uc_mod.Usecase] = Field(default_factory=list)
  # event_steps : List[Action | Decision | ModifyAction | ReadAction | TextReadAction] = Field(default_factory=list)
  # event_steps : List[uc_mod.Action | uc_mod.Decision] = Field(default_factory=list)