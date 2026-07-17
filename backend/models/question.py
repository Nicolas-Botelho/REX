from pydantic import BaseModel, Field
from enum import Enum

class Question(BaseModel):
  question: str