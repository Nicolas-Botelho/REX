from typing import List
from pydantic import BaseModel

class TestCase(BaseModel):
  iD = int
  description = str