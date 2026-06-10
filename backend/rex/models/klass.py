from django.db import models
from polymorphic.models import PolymorphicModel

class Class(PolymorphicModel):
  name = models.CharField(unique=True)
  stereotype = models.CharField(null=True)

class Inheritance(PolymorphicModel):
  parent = models.ForeignKey(Class, related_name='class_parent_in', blank=False, on_delete=models.CASCADE)
  child = models.ForeignKey(Class, related_name='class_child_in', blank=False, on_delete=models.CASCADE)

class Readable(PolymorphicModel):
  pass

class ClassAttribute(Readable):
  name = models.CharField(blank=False)
  types = {'string' : 'string', 'integer' : 'integer', 'boolean' : 'boolean', 'float' : 'float'}
  attr_type = models.CharField(choices=types, blank=False)
  is_multiple = models.BooleanField(default=False)
  valid_values = models.JSONField()
  clazz = models.ForeignKey(Class, related_name='class_attributes', blank=False, on_delete=models.CASCADE)

class AssociationClassReference(PolymorphicModel):
  class_min = models.IntegerField(blank=False)
  class_max = models.IntegerField(blank=True, null=True)
  clazz = models.ForeignKey(Class, related_name='class_associations', blank=False, on_delete=models.CASCADE)

  def delete(self, using = None, keep_parents = False, is_otherside = False):
    if not is_otherside:
      otherside = None
      if hasattr(self, 'acr_as_src'):
        otherside = self.acr_as_src.tgt
      if hasattr(self, 'acr_as_tgt'):
        otherside = self.acr_as_tgt.src
      if otherside:
        otherside.delete(using=using, keep_parents=keep_parents, is_otherside=True)

    return super().delete(using, keep_parents)

class Association(Readable):
  src = models.OneToOneField(AssociationClassReference, related_name='acr_as_src', blank=False, on_delete=models.CASCADE)
  tgt = models.OneToOneField(AssociationClassReference, related_name='acr_as_tgt', blank=False, on_delete=models.CASCADE)