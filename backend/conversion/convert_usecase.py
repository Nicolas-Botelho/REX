from typing import List

from ai_gen.models.usecase import Actor as actor_pyd, Event as event_pyd, Step as step_pyd, Usecase as uc_pyd
from ai_gen.models.response_model.usecase_response import UsecaseOutput

from rex.models.usecase import Actor as actor_dj, Event as event_dj, Step as step_dj, Usecase as uc_dj

class UsecaseConverter():
  def save(self, usecases: UsecaseOutput):
    for uc in usecases.usecases:
      uc_dj.objects.create(
        id = uc.iD,
        name = uc.name
      )
    for actor in usecases.actors:
      actor_dj.objects.create(
        id = actor.iD,
        name = actor.name,
        description = actor.description
      )
    for event in usecases.usecase_events:
      event_dj.objects.create(
        id = event.iD,
        name = event.name,
        actor = event.actor,
        usecase = event.usecase
      )
    for step in usecases.events_steps:
      step_dj.objects.create(
        id = step.iD,
        system = step.system,
        description = step.description,
        event = step.event
      )

  def load():
    pass