from typing import List
from pydantic import BaseModel

class Enum(BaseModel):
  semantic_id : str
  name : str

class EnumAttribute(BaseModel):
  semantic_id : str
  value : str
  enum : str

class Class(BaseModel):
  semantic_id : str
  name : str

class ClassAttributePrim(BaseModel):
  semantic_id : str
  name : str
  attr_type : str
  klass : str

class ClassAttributeEnum(BaseModel):
  semantic_id : str
  name : str
  enum : str
  klass : str

class RelationClassReference(BaseModel):
  semantic_id : str
  minim : int
  maxim : int | None
  ref_class : str

class Relation(BaseModel):
  src : str
  tgt : str