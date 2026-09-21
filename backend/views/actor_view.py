from generation.json_generator import JsonGenerator
from models.requirement import Actor

from fastapi import APIRouter

actor_router = APIRouter(prefix="/actor")

@actor_router.get("/actor/")
def get_actors():
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data.get("actors")}

@actor_router.get("/fr_by_actor/")
def get_requirements_by_actor(name: str):
  jg = JsonGenerator()
  data = jg.return_data()

  frs = data.get("requirement_models").get("functional_requirements")

  return {"data": [fr.get("code") for fr in frs if fr.get("actor_name") == name]}

@actor_router.get("/uc_by_actor/")
def get_usecases_by_actor(name: str):
  jg = JsonGenerator()
  data = jg.return_data()

  ucs = data.get("usecase_models").get("usecases")
  result = []
  for uc in ucs:
    for event in uc.get("usecase_events"):
      if name in event.get("actor_name") and uc.get("name") not in result:
        result.append(uc.get("name"))

  return {"data": result}

@actor_router.post("/actor/")
def create_actor(actor: Actor):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("actors").append(actor.dict())
  jg.write_json(data)

@actor_router.put("/actor/{ac_id}/")
def update_actor(ac_id: int, actor: Actor):
  jg = JsonGenerator()
  data = jg.return_data()

  old_name = data.get("actors")[ac_id].get("name")

  data.get("actors")[ac_id] = actor.dict()

  if old_name != actor.name:
    for fr in data.get("requirement_models").get("functional_requirements"):
      if old_name == fr.get("actor_name"):
        fr["actor_name"] = actor.name
    for uc in data.get("usecase_models").get("usecases"):
      for event in uc.get("usecase_events"):
        if old_name in event.get("actor_name"):
          event.get("actor_name")[event.get("actor_name").index(old_name)] = actor.name

  jg.write_json(data)

@actor_router.delete("/actor/{ac_id}/")
def delete_actor(ac_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  can_del = True

  actor_name = data.get("actors")[ac_id].get("name")

  for fr in data.get("requirement_models").get("functional_requirements"):
    if actor_name == fr.get("actor_name"):
      can_del = False
  for uc in data.get("usecase_models").get("usecases"):
    for event in uc.get("usecase_events"):
      if actor_name in event.get("actor_name"):
        can_del = False
  
  if can_del:
    data.get("actors").pop(ac_id)
    jg.write_json(data)