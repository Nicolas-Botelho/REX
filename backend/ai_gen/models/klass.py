from typing import List
from pydantic import BaseModel, Field
from enum import Enum

class InheritanceClassReference(BaseModel):
  pass

class Inheritance(BaseModel):
  parent_class_name : str
  child_class_name : str

class AssociationClassReference(BaseModel):
  class_name : str
  class_min : int
  class_max : int | None

class Association(BaseModel):
  src : AssociationClassReference
  tgt : AssociationClassReference

class TypeEnum(str, Enum):
  STRING = "string"
  INTEGER = "integer"
  BOOLEAN = "boolean"
  FLOAT = "float"

class ClassAttribute(BaseModel):
  name : str
  attr_type : TypeEnum
  is_multiple : bool
  valid_values : List[str] = Field(default_factory=list)

class StereotypeEnum(str, Enum):
  KIND = "kind"
  SUBKIND = "subkind"
  ROLE = "role"

class Class(BaseModel):
  name : str
  stereotype : StereotypeEnum
  class_attributes : List[ClassAttribute] = Field(default_factory=list)