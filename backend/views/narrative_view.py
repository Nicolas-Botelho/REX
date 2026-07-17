from generation.json_generator import JsonGenerator

from fastapi import APIRouter

narrative_router = APIRouter(prefix="/narrative")

@narrative_router.get("/narrative/")
def get_narrative() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("narrative_models").get("domain_narrative")}

@narrative_router.get("/questions")
def get_narrative_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("narrative_models").get("questions")}