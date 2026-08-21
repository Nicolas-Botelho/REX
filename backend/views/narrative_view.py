from generation.json_generator import JsonGenerator
from models.requirement import DomainNarrative
from models.question import NarrativeQuestion

from fastapi import APIRouter

narrative_router = APIRouter(prefix="/narrative")

#############
# Narrative #
#############

@narrative_router.get("/narrative/")
def get_narrative() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("narrative_models").get("domain_narrative")}

@narrative_router.put("/narrative/")
def update_narrative(narrative: DomainNarrative):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("narrative_models")["domain_narrative"] = narrative.dict()
  jg.write_json(data)

@narrative_router.delete("/narrative/")
def delete_narrative():
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("narrative_models")["domain_narrative"] = DomainNarrative(narrative="").dict()
  jg.write_json(data)

############
# Question #
############

@narrative_router.get("/questions/")
def get_narrative_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("narrative_models").get("questions")}

@narrative_router.post("/questions/")
def create_narrative_question(question: NarrativeQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("narrative_models").get("questions").append(question.dict())
  jg.write_json(data)

@narrative_router.put("/questions/{q_id}/")
def update_narrative_question(q_id: int, question: NarrativeQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("narrative_models").get("questions")[q_id] = question.dict()
  jg.write_json(data)

@narrative_router.delete("/questions/{q_id}/")
def delete_narrative_question(q_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("narrative_models").get("questions").pop(q_id)
  jg.write_json(data)