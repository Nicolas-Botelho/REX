from typing import List
from pydantic import BaseModel, Field

class ref_Class(BaseModel):
  id : int
  name : str

class ref_RelationClassReference(BaseModel):
  id : int
  minim : int
  maxim : int | None
  ref_class : ref_Class

class Relation(BaseModel):
  id : int
  src : ref_RelationClassReference
  tgt : ref_RelationClassReference  

class RelationClassReference(BaseModel):
  id : int
  rcr_as_src : Relation | None
  rcr_as_tgt : Relation | None
  minim : int
  maxim : int | None
  ref_class : ref_Class

class Inheritance(BaseModel):
  id : int
  parent : ref_Class
  child : ref_Class

class ref_Enum(BaseModel):
  id : int
  name : str

class EnumValue(BaseModel):
  id : int
  value : str
  enum : ref_Enum

class Enum(BaseModel):
  id : int
  enum_values : List[EnumValue] = Field(default_factory=list)
  name : str

class ClassAttributeEnum(BaseModel):
  id : int
  enum : Enum
  name : str
  klass : int

class ClassAttributePrim(BaseModel):
  id : int
  name : str
  attr_type : str
  klass : int

class Class(BaseModel):
  id : int
  class_attrs : List[ClassAttributeEnum | ClassAttributePrim] = Field(default_factory=list)
  class_relations : List[RelationClassReference] = Field(default_factory=list)
  class_parents : List[Inheritance] = Field(default_factory=list)
  class_childs : List[Inheritance] = Field(default_factory=list)
  name : str
  stereotype : str | None