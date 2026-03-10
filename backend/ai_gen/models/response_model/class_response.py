from ai_gen.models.klass import Enum, EnumAttribute, Class, ClassAttributeEnum, ClassAttributePrim, Relation, RelationClassReference

from typing import List
from pydantic import BaseModel, Field

class ClassOutput(BaseModel):
  enums : List[Enum] = Field(default_factory=list)
  enum_attributes : List[EnumAttribute] = Field(default_factory=list)
  classes : List[Class] = Field(default_factory=list)
  class_enum_attributes : List[ClassAttributeEnum] = Field(default_factory=list)
  class_primitive_attributes : List[ClassAttributePrim] = Field(default_factory=list)
  relation_class_references : List[RelationClassReference] = Field(default_factory=list)
  relations : List[Relation] = Field(default_factory=list)
