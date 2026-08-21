from models.requirement import DomainNarrative
from models.question import NarrativeQuestion

from pydantic import BaseModel, Field

class NarrativeOutput(BaseModel):
  domain_narrative: DomainNarrative
  questions: list[NarrativeQuestion] = Field(default_factory=list)