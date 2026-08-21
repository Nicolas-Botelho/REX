from generation.json_generator import JsonGenerator
from models.usecase import Usecase
from models.question import UsecaseQuestion

from fastapi import APIRouter, Response, status

usecase_router = APIRouter(prefix="/usecases")

###########
# Usecase #
###########

@usecase_router.get("/usecase/")
def get_usecases():
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data.get("usecase_models").get("usecases")}

@usecase_router.get("/usecase/{uc_id}/")
def get_usecase(uc_id: int, response: Response):
  jg = JsonGenerator()
  data = jg.return_data()

  usecases = data.get("usecase_models").get("usecases")

  if uc_id >= 0 and uc_id < len(usecases):
    return {"data": usecases[uc_id]}
  else:
    response.status_code = status.HTTP_404_NOT_FOUND
    return

@usecase_router.post("/usecase/")
def create_usecase(uc: Usecase):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("usecase_models").get("usecases").append(uc.dict())
  jg.write_json(data)

@usecase_router.put("/usecase/{uc_id}/")
def update_usecase(uc_id: int, uc: Usecase):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("usecase_models").get("usecases")[uc_id] = uc.dict()
  jg.write_json(data)

@usecase_router.delete("/usecase/{uc_id}/")
def delete_usecase(uc_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("usecase_models").get("usecases").pop(uc_id)
  jg.write_json(data)

############
# Question #
############

@usecase_router.get("/questions/")
def get_usecase_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("usecase_models").get("questions")}

@usecase_router.post("/questions/")
def create_usecase_question(question: UsecaseQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("usecase_models").get("questions").append(question.dict())
  jg.write_json(data)

@usecase_router.put("/questions/{q_id}/")
def update_usecase_question(q_id: int, question: UsecaseQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("usecase_models").get("questions")[q_id] = question.dict()
  jg.write_json(data)

@usecase_router.delete("/questions/{q_id}/")
def delete_usecase_question(q_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("usecase_models").get("questions").pop(q_id)
  jg.write_json(data)