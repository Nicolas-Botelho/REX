from django.db import models

from polymorphic.models import PolymorphicModel

class Usecase(PolymorphicModel):
  name = models.CharField(blank=False)

class Actor(PolymorphicModel):
  name = models.CharField(blank=False)
  description = models.TextField(blank=True, null=True)

class Event(PolymorphicModel):
  name = models.CharField(blank=False)
  usecase = models.ForeignKey(Usecase, related_name="usecase_events", blank=False, on_delete=models.CASCADE)
  actor = models.ForeignKey(Actor, related_name="actor_events", blank=False, on_delete=models.PROTECT)

class Step(PolymorphicModel):
  system = models.BooleanField(blank=False)    # True if the step is a System Action, False if it is a Actor Action
  description = models.TextField(blank=False)
  event = models.ForeignKey(Event, related_name="event_steps", blank=False, on_delete=models.CASCADE)