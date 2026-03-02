from ai_gen.models.test_case import TestCase

from typing import List
from pydantic import BaseModel

class TCOutput(BaseModel):
  tc_list : List[TestCase]
