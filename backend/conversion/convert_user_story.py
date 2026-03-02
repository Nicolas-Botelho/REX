from typing import List

from ai_gen.models.user_story import Epic as Epic_pydantic, UserStory as US_pydantic, Actor as Actor_pydantic
from ai_gen.response_model.user_story_response import EpicOutput, USOutput, ActorOutput

from rex.models.userstory import Epic as Epic_django, UserStory as US_django, Actor as Actor_django

# class TC_converter():
#   def save_tc(tc_list: TCOutput):
#     for tc in tc_list.tc_list:
#       TC_django.objects.create(
#         description = tc.description
#       )

#   def load_tc(tc_list : List[TC_django]) -> TCOutput:
#     out = TCOutput([])

#     for tc in tc_list:
#       tc_pyd = TC_pydantic()
#       tc_pyd.iD = tc.iD
#       tc_pyd.description = tc.description

#       out.tc_list.append(tc_pyd)

#     return out

class Epic_converter():
  def save_epic(epic_list: EpicOutput):
    for epic in epic_list.epic_list:
      Epic_django.objects.create(
        userStories = epic.userStories
      )

  def load_epic(epic_list: List[Epic_django]) -> EpicOutput:
    out = EpicOutput([])

    for epic in epic_list:
      epic_pyd = Epic_pydantic()
      epic_pyd.iD = epic.iD
      epic_pyd.userStories = epic.userStories

      out.epic_list.append(epic_pyd)
    
    return out

class US_converter():
  def save_US(us_list: USOutput):
    for us in us_list.us_list:
      US_django.objects.create(
        goal = us.goal,
        action = us.action,
        performer = us.performer
      )

  def load_US(us_list: List[US_django]) -> USOutput:
    out = USOutput([])

    for us in us_list:
      us_pyd = US_pydantic()
      us_pyd.iD = us.iD
      us_pyd.goal = us.goal
      us_pyd.action = us.action
      us_pyd.performer = us.performer

      out.us_list.append(us_pyd)
    
    return out

class Actor_converter():
  def save_Actor(actor_list: ActorOutput):
    for actor in actor_list.actor_list:
      Actor_django.objects.create(
        name = actor.name
      )

  def load_Actor(actor_list: List[Actor_django]) -> ActorOutput:
    out = ActorOutput([])

    for actor in actor_list:
      actor_pyd = Actor_pydantic()
      actor_pyd.iD = actor.iD
      actor_pyd.name = actor.name

      out.actor_list.append(actor_pyd)

    return out