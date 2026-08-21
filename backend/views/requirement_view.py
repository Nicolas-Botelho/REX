from generation.json_generator import JsonGenerator
from models.requirement import FunctionalRequirement, NonFunctionalRequirement, BusinessRule
from models.question import RequirementQuestion

from fastapi import APIRouter

requirement_router = APIRouter(prefix="/requirements")

######
# FR #
######

@requirement_router.get("/functional_requirement/")
def get_FRs() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("requirement_models").get("functional_requirements")}

@requirement_router.post("/functional_requirement/")
def create_FR(fr: FunctionalRequirement):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("functional_requirements").append(fr.dict())
  jg.write_json(data)

@requirement_router.put("/functional_requirement/{fr_id}/")
def update_FR(fr_id: int, fr: FunctionalRequirement):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("functional_requirements")[fr_id] = fr.dict()
  jg.write_json(data)

@requirement_router.delete("/functional_requirement/{fr_id}/")
def delete_FR(fr_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  frs = data.get("requirement_models").get("functional_requirements")
  nfrs = data.get("requirement_models").get("non_functional_requirements")
  ucs = data.get("usecase_models").get("usecases")

  req: dict = frs.pop(fr_id)

  req_code = req.get("code")

  for fr in frs:
    dependencies: list = fr.get("depends_on_requirements_codes")
    if req_code in dependencies:
      dependencies.remove(req_code)
  for nfr in nfrs:
    applications: list = nfr.get("applies_on_requirements_codes")
    if req_code in applications:
      applications.remove(req_code)
  for uc in ucs:
    events: list = uc.get("usecase_events")
    for event in events:
      dependencies: list = event.get("functional_requirements_codes")
      if req_code in dependencies:
        dependencies.remove(req_code)

  jg.write_json(data)

#######
# NFR #
#######

@requirement_router.get("/non_functional_requirement/")
def get_NFRs() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("requirement_models").get("non_functional_requirements")}

@requirement_router.post("/non_functional_requirement")
def create_NFR(nfr: NonFunctionalRequirement):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("non_functional_requirements").append(nfr.dict())
  jg.write_json(data)

@requirement_router.put("/non_functional_requirement/{nfr_id}/")
def update_NFR(nfr_id: int, nfr: NonFunctionalRequirement):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("non_functional_requirements")[nfr_id] = nfr.dict()
  jg.write_json(data)

@requirement_router.delete("/non_functional_requirement/{nfr_id}/")
def delete_NFR(nfr_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("non_functional_requirements").pop(nfr_id)
  jg.write_json(data)

######
# BR #
######

@requirement_router.get("/business_rule/")
def get_BRs() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("requirement_models").get("business_rules")}

@requirement_router.post("/business_rule/")
def create_BR(br: BusinessRule):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("business_rules").append(br.dict())
  jg.write_json(data)

@requirement_router.put("/business_rule/{br_id}/")
def update_BR(br_id: int, br: BusinessRule):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("business_rules")[br_id] = br.dict()
  jg.write_json(data)

@requirement_router.delete("/business_rule/{br_id}/")
def delete_BR(br_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  frs = data.get("requirement_models").get("functional_requirements")

  req: dict = data.get("requirement_models").get("business_rules").pop(br_id)
  req_code = req.get("code")

  for fr in frs:
    dependencies: list = fr.get("apply_business_rules_codes")
    if req_code in dependencies:
      dependencies.remove(req_code)

  jg.write_json(data)

############
# Question #
############

@requirement_router.get("/questions/")
def get_requirement_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("requirement_models").get("questions")}

@requirement_router.post("/questions/")
def create_requirement_question(question: RequirementQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("questions").append(question.dict())
  jg.write_json(data)

@requirement_router.put("/questions/{q_id}/")
def update_requirement_question(q_id: int, question: RequirementQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("questions")[q_id] = question.dict()
  jg.write_json(data)

@requirement_router.delete("/questions/{q_id}/")
def delete_requirement_question(q_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("requirement_models").get("questions").pop(q_id)
  jg.write_json(data)