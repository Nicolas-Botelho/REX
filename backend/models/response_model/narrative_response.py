from models.requirement import DomainNarrative
from models.question import Question

from pydantic import BaseModel, Field

class NarrativeOutput(BaseModel):
  domain_narrative: DomainNarrative
  questions: list[Question] = Field(default_factory=list)