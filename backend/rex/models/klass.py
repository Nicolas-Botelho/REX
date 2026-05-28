from django.db import models
from polymorphic.models import PolymorphicModel

class Enum(PolymorphicModel):
  name = models.CharField(unique=True, blank=False)

class EnumAttribute(PolymorphicModel):
  value = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_values', blank=False, on_delete=models.CASCADE)

class Class(PolymorphicModel):
  name = models.CharField(unique=True, blank=False)
  stereotype = models.CharField(blank=True, null=True)

class Inheritance(PolymorphicModel):
  parent = models.ForeignKey(Class, related_name='class_parents', blank=False, on_delete=models.CASCADE)
  child = models.ForeignKey(Class, related_name='class_childs', blank=False, on_delete=models.CASCADE)

class Readable(PolymorphicModel):
  pass

class ClassAttribute(Readable):
  name = models.CharField(blank=False)
  klass = models.ForeignKey(Class, related_name='class_attrs', blank=False, on_delete=models.CASCADE)

class ClassAttributePrim(ClassAttribute):
  primitive_types = {'string' : 'string', 'integer' : 'integer', 'boolean' : 'boolean', 'float' : 'float'}
  attr_type = models.CharField(choices=primitive_types, blank=False)

class ClassAttributeEnum(ClassAttribute):
  enum = models.ForeignKey(Enum, related_name='enum_related_classes', blank=False, on_delete=models.PROTECT)

class RelationClassReference(PolymorphicModel):
  minim = models.IntegerField(blank=False)
  maxim = models.IntegerField(blank=True, null=True)
  ref_class = models.ForeignKey(Class, related_name='class_relations', blank=False, on_delete=models.CASCADE)

  def delete(self, using = None, keep_parents = False, is_otherside = False):
    if not is_otherside:
      otherside = None
      if hasattr(self, 'rcr_as_src'):
        otherside = self.rcr_as_src.tgt
      if hasattr(self, 'rcr_as_tgt'):
        otherside = self.rcr_as_tgt.src
      if otherside:
        otherside.delete(using=using, keep_parents=keep_parents, is_otherside=True)

    return super().delete(using, keep_parents)

class Relation(Readable):
  src = models.OneToOneField(RelationClassReference, related_name='rcr_as_src', blank=False, on_delete=models.CASCADE)
  tgt = models.OneToOneField(RelationClassReference, related_name='rcr_as_tgt', blank=False, on_delete=models.CASCADE)