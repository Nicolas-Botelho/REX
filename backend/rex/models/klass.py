from django.db import models
from polymorphic.models import PolymorphicModel

class Enum(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(unique=True, blank=False)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class EnumAttribute(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  value = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_values', blank=False, on_delete=models.CASCADE)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class Class(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(unique=True, blank=False)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class ClassAttributePrim(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(blank=False)
  primitive_types = {'string' : 'string', 'integer' : 'integer', 'boolean' : 'boolean', 'float' : 'float'}
  attr_type = models.CharField(choices=primitive_types, blank=False)
  klass = models.ForeignKey(Class, related_name='class_primitive_attrs', blank=False, on_delete=models.CASCADE)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class ClassAttributeEnum(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_related_classes', blank=False, on_delete=models.PROTECT)
  klass = models.ForeignKey(Class, related_name='class_enum_attrs', blank=False, on_delete=models.CASCADE)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class RelationClassReference(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  minim = models.IntegerField(blank=False)
  maxim = models.IntegerField(blank=True, null=True)
  ref_class = models.ForeignKey(Class, related_name='class_relations', blank=False, on_delete=models.CASCADE)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class Relation(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  src = models.ForeignKey(RelationClassReference, related_name='rcr_as_srcs', blank=False, on_delete=models.CASCADE)
  tgt = models.ForeignKey(RelationClassReference, related_name='rcr_as_tgts', blank=False, on_delete=models.CASCADE)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])