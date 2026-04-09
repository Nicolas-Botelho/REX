from django.db import models

from polymorphic.models import PolymorphicModel

class Usecase(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(blank=False)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class Actor(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(blank=False)
  description = models.TextField(max_length=256, blank=True, null=True)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class Event(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  name = models.CharField(blank=False)
  usecase = models.ForeignKey(Usecase, related_name="usecase_events", blank=False, on_delete=models.CASCADE)
  actor = models.ForeignKey(Actor, related_name="actor_events", blank=False, on_delete=models.PROTECT)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])

class Step(PolymorphicModel):
  ref_id = models.PositiveIntegerField(unique=True, null=True, blank=False)
  system = models.BooleanField(blank=False)    # True if the step is a System Action, False if it is a Actor Action
  description = models.TextField(max_length=256, blank=False)
  event = models.ForeignKey(Event, related_name="event_steps", blank=False, on_delete=models.CASCADE)

  def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
    super().save(force_insert, force_update, using, update_fields)

    if self.ref_id == None:
      self.ref_id = self.id
      super().save(update_fields=['ref_id'])