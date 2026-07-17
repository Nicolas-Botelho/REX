from generation.json_generator import JsonGenerator

from fastapi import APIRouter

requirement_router = APIRouter(prefix="/requirements")

@requirement_router.get("/requirement/")
def get_requirements() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("requirement_models").get("requirements")}

@requirement_router.get("/functional_requirement")
def get_FRs() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  requirements = data.get("requirement_models").get("requirements")

  return {"data": [req for req in requirements if req.get("requirement_type") == "functional_requirement"]}

@requirement_router.get("/non_functional_requirement")
def get_NFRs() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  requirements = data.get("requirement_models").get("requirements")

  return {"data": [req for req in requirements if req.get("requirement_type") == "non_functional_requirement"]}

@requirement_router.get("/business_rule")
def get_BRs() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  requirements = data.get("requirement_models").get("requirements")

  return {"data": [req for req in requirements if req.get("requirement_type") == "business_rules"]}

@requirement_router.get("/questions")
def get_requirement_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("requirement_models").get("questions")}