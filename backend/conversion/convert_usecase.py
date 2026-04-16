from typing import List

from ai_gen.models.usecase import Actor as Actor_pyd, Event as Event_pyd, Step as Step_pyd, Usecase as UC_pyd
from ai_gen.models.response_model.usecase_response import UsecaseOutput

from rex.models.usecase import Actor as Actor_dj, Event as Event_dj, Step as Step_dj, Usecase as UC_dj

from conversion.utils.case import snake_case

class UsecaseConverter():
  def save(self, usecases: UsecaseOutput):
    uc_map = {}
    actor_map = {}
    event_map = {}

    for uc in usecases.usecases:
      new_uc = UC_dj.objects.create(
        name = uc.name
      )
      uc_map[uc.semantic_id] = new_uc.id
    for actor in usecases.actors:
      new_actor = Actor_dj.objects.create(
        name = actor.name,
        description = actor.description
      )
      actor_map[actor.semantic_id] = new_actor.id
    for event in usecases.usecase_events:
      Event_dj.objects.create(
        name = event.name,
        actor_id = actor_map[event.actor],
        usecase_id = uc_map[event.usecase]
      )
    for step in usecases.events_steps:
      Step_dj.objects.create(
        system = step.system,
        description = step.description,
        event_id = event_map[step.event]
      )

  def load(self):
    output = UsecaseOutput()

    for uc in UC_dj.objects.all():
      snake_uc_name = snake_case(uc.name)
      uc_pyd = UC_pyd(semantic_id=snake_uc_name, name=uc.name)
      output.usecases.append(uc_pyd)

      for event in uc.usecase_events.all():
        snake_event_name = snake_case(event.name)
        snake_actor_name = snake_case(event.actor.name)

        event_pyd = Event_pyd(semantic_id=snake_event_name, name=event.name, usecase=snake_uc_name, actor=snake_actor_name)
        output.usecase_events.append(event_pyd)

        actor_pyd = Actor_pyd(semantic_id=snake_actor_name, name=event.actor.name, description=event.actor.description)
        output.actors.append(actor_pyd)

        step_count = 1
        for step in event.event_steps.all():
          step_pyd = Step_pyd(semantic_id=f"{snake_event_name}_step_{step_count}", system=step.system, description=step.description, event=snake_event_name)
          output.events_steps.append(step_pyd)
          step_count += 1
    
    return output