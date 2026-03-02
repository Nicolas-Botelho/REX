from ai_gen.models.user_story import Epic, UserStory, Actor

from typing import List
from pydantic import BaseModel

class EpicOutput(BaseModel):
  epic_list : List[Epic]

class USOutput(BaseModel):
  us_list : List[UserStory]

class ActorOutput(BaseModel):
  actor_list : List[Actor]