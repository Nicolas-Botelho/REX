from django.db import models

from polymorphic.models import PolymorphicModel

from rex.models.klass import Class, Readable

class Usecase(PolymorphicModel):
  name = models.CharField(blank=False)

class Actor(PolymorphicModel):
  name = models.CharField(blank=False)
  description = models.TextField(blank=True, null=True)

class Event(PolymorphicModel):
  name = models.CharField(blank=False)
  # description = models.CharField(blank=False)
  usecase = models.ForeignKey(Usecase, related_name='usecase_events', blank=False, on_delete=models.CASCADE)
  actor = models.ForeignKey(Actor, related_name='actor_events', blank=False, on_delete=models.PROTECT)
  # first_step = models.ForeignKey(Step, related_name='step_first_step', null=True, on_delete=models.PROTECT)

class Step(PolymorphicModel):
  step_code = models.TextField(unique=True)
  description = models.TextField()
  clazz = models.ForeignKey(Class, related_name="class_steps", blank=False, null=True, on_delete=models.PROTECT)
  event = models.ForeignKey(Event, related_name="event_steps", blank=False, on_delete=models.CASCADE)

class Action(Step):
  next_step = models.ForeignKey(Step, related_name='past_step', blank=False, null=True, on_delete=models.CASCADE)
  category = models.TextField(null=True)

class Decision(Step):
  next_steps = models.ManyToManyField(Step, related_name='past_steps', blank=False)