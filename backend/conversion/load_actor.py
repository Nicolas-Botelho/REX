import models.requirement as pyd
from generation.json_reader import JsonReader

class ActorLoader():
  def load(self):
    json_r = JsonReader()
    actor_models = json_r.read().get("actors")

    if actor_models == None:
      return []

    return self.load_actors(actor_models)

  def load_actors(self, models: list) -> list[pyd.Actor]:
    actors: list[pyd.Actor] = []
    for model in models:
      try:
        actors.append(pyd.Actor.model_validate(model))
      except Exception as e:
        print(f"INVALID ACTOR {e}: {model}")
    return actors