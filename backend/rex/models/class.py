from django.db import models

class Enum(models.Model):
  iD = models.IntegerField(unique=True, blank=False)
  name = models.CharField(unique=True, blank=False)

class EnumAttribute(models.Model):
  iD = models.IntegerField(unique=True, blank=False)
  value = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_values', blank=False, on_delete=models.CASCADE)

class Class(models.Model):
  iD = models.IntegerField(unique=True, blank=False)
  name = models.CharField(unique=True, blank=False)

class ClassAttributePrim(models.Model):
  iD = models.IntegerField(unique=True, blank=False)
  name = models.CharField(blank=False)
  primitive_types = {'str' : 'string', 'int' : 'integer', 'bool' : 'boolean', 'float' : 'float'}
  attr_type = models.CharField(choices=primitive_types, blank=False)
  klass = models.ForeignKey(Class, related_name='class_primitive_attrs', blank=False, on_delete=models.CASCADE)

class ClassAttributeEnum(models.Model):
  iD = models.IntegerField(unique=True, blank=False)
  name = models.CharField(blank=False)
  enum = models.ForeignKey(Enum, related_name='enum_related_classes', blank=False, on_delete=models.PROTECT)
  klass = models.ForeignKey(Class, related_name='class_enum_attrs', blank=False, on_delete=models.CASCADE)

class RelationClassReference():
  iD = models.IntegerField(unique=True, blank=False)
  minim = models.IntegerField(blank=False)
  maxim = models.IntegerField(blank=False)
  ref_class = models.ForeignKey(Class, related_name='class_relations', blank=False, on_delete=models.CASCADE)

class Relation():
  iD = models.IntegerField(unique=True, blank=False)
  src = models.ForeignKey(RelationClassReference, related_name='rcr_as_srcs', blank=False, on_delete=models.CASCADE)
  tgt = models.ForeignKey(RelationClassReference, related_name='rcr_as_tgts', blank=False, on_delete=models.CASCADE)