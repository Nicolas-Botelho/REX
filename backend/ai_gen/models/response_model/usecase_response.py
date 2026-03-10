from ai_gen.models.usecase import Actor, Event, Step, Usecase

from typing import List
from pydantic import BaseModel, Field

class UsecaseOutput(BaseModel):
  actors : List[Actor] = Field(default_factory=list)
  usecase_events : List[Event] = Field(default_factory=list)
  events_steps : List[Step] = Field(default_factory=list)
  usecases : List[Usecase] = Field(default_factory=list)