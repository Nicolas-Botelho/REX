from models.usecase import Usecase
from models.question import Question

from pydantic import BaseModel, Field

class UsecaseOutput(BaseModel):
  usecases : list[Usecase] = Field(default_factory=list)
  questions : list[Question] = Field(default_factory=list)
  # event_steps : List[Action | Decision | ModifyAction | ReadAction | TextReadAction] = Field(default_factory=list)
  # event_steps : List[uc_mod.Action | uc_mod.Decision] = Field(default_factory=list)