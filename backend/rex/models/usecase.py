from django.db import models

from polymorphic.models import PolymorphicModel

from rex.models.klass import Class, Readable

class Usecase(PolymorphicModel):
  name = models.CharField(blank=False)

class Actor(PolymorphicModel):
  name = models.CharField(blank=False)
  description = models.TextField(blank=True, null=True)

class Step(PolymorphicModel):
  description = models.TextField(blank=True, null=True)

class Event(PolymorphicModel):
  name = models.CharField(blank=False)
  usecase = models.ForeignKey(Usecase, related_name='usecase_events', blank=False, on_delete=models.CASCADE)
  actor = models.ForeignKey(Actor, related_name='actor_events', blank=False, on_delete=models.PROTECT)
  first_step = models.ForeignKey(Step, related_name='step_first_step', null=True, on_delete=models.PROTECT)

class Action(Step):
  next_step = models.ForeignKey(Step, related_name='past_step', blank=False, null=True, on_delete=models.CASCADE)

class Decision(Step):
  next_steps = models.ManyToManyField(Step, related_name='past_steps', blank=False)

class ClassManipulationAction(Action):
  related_classes = models.ManyToManyField(Class, related_name='class_related_classes', blank=False)

class ModifyAction(ClassManipulationAction):
  action_type = models.CharField(choices={'create': 'create', 'update': 'update', 'delete': 'delete'})

class ReadAction(ClassManipulationAction):
  read_attributes = models.ManyToManyField(Readable, related_name='readable_read_attributes', blank=False)

class TextReadAction(ReadAction):
  match_percent = models.FloatField(blank=False, null=False)