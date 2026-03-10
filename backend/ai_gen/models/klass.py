from typing import List
from pydantic import BaseModel

class Enum(BaseModel):
  iD : int
  name : str

class EnumAttribute(BaseModel):
  iD : int
  value : str
  enum : int

class Class(BaseModel):
  iD : int
  name : str

class ClassAttributePrim(BaseModel):
  iD : int
  name : str
  attr_type : str
  klass : int

class ClassAttributeEnum(BaseModel):
  iD : int
  name : str
  enum : int
  klass : int

class RelationClassReference(BaseModel):
  iD : int
  minim : int
  maxim : int
  ref_class : int

class Relation(BaseModel):
  iD : int
  src : int
  tgt : int