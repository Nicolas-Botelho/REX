from typing import List

from ai_gen.models.usecase import Actor as Actor_pyd, Event as Event_pyd, Step as Step_pyd, Usecase as UC_pyd
from ai_gen.models.response_model.usecase_response import UsecaseOutput

from rex.models.usecase import Actor as Actor_dj, Event as Event_dj, Step as Step_dj, Usecase as UC_dj

class UsecaseConverter():
  def save(self, usecases: UsecaseOutput):
    for uc in usecases.usecases:
      UC_dj.objects.create(
        id = uc.iD,
        name = uc.name
      )
    for actor in usecases.actors:
      Actor_dj.objects.create(
        id = actor.iD,
        name = actor.name,
        description = actor.description
      )
    for event in usecases.usecase_events:
      Event_dj.objects.create(
        id = event.iD,
        name = event.name,
        actor_id = event.actor,
        usecase_id = event.usecase
      )
    for step in usecases.events_steps:
      Step_dj.objects.create(
        id = step.iD,
        system = step.system,
        description = step.description,
        event_id = step.event
      )

  def load(self):
    output = UsecaseOutput()

    for uc in UC_dj.objects.all():
      uc_pyd = UC_pyd(iD=uc.id, name=uc.name)
      output.usecases.append(uc_pyd)

      for event in uc.usecase_events.all():
        event_pyd = Event_pyd(iD=event.id, name=event.name, usecase=event.usecase, actor=event.actor.id)
        output.usecase_events.append(event_pyd)

        actor_pyd = Actor_pyd(iD=event.actor.id, name=event.actor.name, description=event.actor.description)
        output.actors.append(actor_pyd)

        for step in event.event_steps.all():
          step_pyd = Step_pyd(iD=step.id, system=step.system, description=step.description, event=step.event)
          output.events_steps.append(step_pyd)