from typing import List
from pydantic import BaseModel, Field
from enum import Enum as MetaEnum

class Association(BaseModel):
  src_class_name : str
  src_class_min : int
  src_class_max : int | None
  tgt_class_name : str
  tgt_class_min : int
  tgt_class_max : int | None