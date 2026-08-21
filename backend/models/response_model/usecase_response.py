from models.usecase import Usecase
from models.requirement import Actor
from models.question import UsecaseQuestion

from pydantic import BaseModel, Field

class UsecaseOutput(BaseModel):
  usecases : list[Usecase] = Field(default_factory=list)
  actors: list[Actor] = Field(default_factory=list)
  questions : list[UsecaseQuestion] = Field(default_factory=list)