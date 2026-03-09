from django.db import models
from polymorphic.models import PolymorphicModel

class Enum(PolymorphicModel):
  name = models.CharField(unique=True, blank=False)

class EnumAttribute(PolymorphicModel):
  value = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_values', blank=False, on_delete=models.CASCADE)

class Class(PolymorphicModel):
  name = models.CharField(unique=True, blank=False)

class ClassAttributePrim(PolymorphicModel):
  name = models.CharField(blank=False)
  primitive_types = {'str' : 'string', 'int' : 'integer', 'bool' : 'boolean', 'float' : 'float'}
  attr_type = models.CharField(choices=primitive_types, blank=False)
  klass = models.ForeignKey(Class, related_name='class_primitive_attrs', blank=False, on_delete=models.CASCADE)

class ClassAttributeEnum(PolymorphicModel):
  name = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_related_classes', blank=False, on_delete=models.PROTECT)
  klass = models.ForeignKey(Class, related_name='class_enum_attrs', blank=False, on_delete=models.CASCADE)

class RelationClassReference(PolymorphicModel):
  minim = models.IntegerField(blank=False)
  maxim = models.IntegerField(blank=False)
  ref_class = models.ForeignKey(Class, related_name='class_relations', blank=False, on_delete=models.CASCADE)

class Relation(PolymorphicModel):
  src = models.ForeignKey(RelationClassReference, related_name='rcr_as_srcs', blank=False, on_delete=models.CASCADE)
  tgt = models.ForeignKey(RelationClassReference, related_name='rcr_as_tgts', blank=False, on_delete=models.CASCADE)