from generation.json_generator import JsonGenerator

from fastapi import APIRouter

usecase_router = APIRouter(prefix="/usecases")

@usecase_router.get("/usecase/")
def get_usecases():
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data.get("usecase_models").get("usecases")}

@usecase_router.get("/usecase/{id}")
def get_usecase(id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  usecases = data.get("usecase_models").get("usecases")

  if id >= 0 and id < len(usecases):
    return {"data": usecases[id]}
  else:
    response.status_code = status.HTTP_404_NOT_FOUND
    return

@usecase_router.get("/questions")
def get_usecase_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("usecase_models").get("questions")}