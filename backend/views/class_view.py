from generation.json_generator import JsonGenerator

from fastapi import APIRouter, Response, status

class_router = APIRouter(prefix="/classes")

#########
# Class #
#########

@class_router.get("/class/")
def get_classes() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data.get("class_models").get("classes")}

@class_router.get("/class/{id}/")
def get_class(id: int, response: Response) -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  classes = data.get("class_models").get("classes")
  
  if id >= 0 and id < len(classes):
    return {"data": classes[id]}
  else:
    response.status_code = status.HTTP_404_NOT_FOUND
    return

@class_router.get("/class_by_name/")
def get_class_by_name(class_name: str) -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  classes = data.get("class_models").get("classes")
  filtered = []

  for clazz in classes:
    if clazz.get("name") == class_name:
      clazz["index"] = classes.index(clazz)
      filtered.append(clazz)
  
  return {"data": filtered}

@class_router.get("/questions")
def get_class_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("class_models").get("questions")}

###############
# Association #
###############

@class_router.get("/association/")
def get_associations():
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data.get("class_models").get("associations")}

@class_router.get("/association/{id}/")
def get_association(id: int):
  jg = JsonGenerator()
  data = jg.return_data()
  
  associations = data.get("class_models").get("associations")

  if id >= 0 and id < len(associations):
    return {"data": associations[id]}
  else:
    response.status_code = status.HTTP_404_NOT_FOUND
    return

@class_router.get("/class_associations/")
def get_class_associations(class_name: str):
  jg = JsonGenerator()
  data = jg.return_data()

  associations = data.get("class_models").get("associations")
  class_associations = []

  for association in associations:
    if association.get("src").get("class_name") == class_name or association.get("tgt").get("class_name") == class_name:
      class_associations.append(association)
  
  return {"data": class_associations}

###############
# Inheritance #
###############

@class_router.get("/inheritance/")
def get_inheritances():
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data.get("class_models").get("inheritances")}

@class_router.get("/inheritance/{id}/")
def get_inheritance(id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  inheritances = data.get("class_models").get("inheritances")

  if id >= 0 and id < len(inheritances):
    return {"data": inheritances[id]}
  else:
    response.status_code = status.HTTP_404_NOT_FOUND
    return

@class_router.get("/class_inheritances/")
def get_class_inheritances(class_name: str):
  jg = JsonGenerator()
  data = jg.return_data()

  inheritances = data.get("class_models").get("inheritances")
  class_inheritances = []

  for inheritance in inheritances:
    if inheritance.get("parent_class_name") == class_name or inheritance.get("child_class_name") == class_name:
      class_inheritances.append(inheritance)
  
  return {"data": class_inheritances}