from generation.json_generator import JsonGenerator
from models.klass import Class, Association, Inheritance
from models.question import ClassQuestion

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

@class_router.post("/class/")
def create_class(klass: Class):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("classes").append(klass.dict())
  jg.write_json(data)

@class_router.put("/class/{cls_id}/")
def update_class(cls_id: int, klass: Class):
  jg = JsonGenerator()
  data = jg.return_data()

  old_name = data.get("class_models").get("classes")[cls_id].get("name")
  
  ucs = data.get("usecase_models").get("usecases")
  assocs = data.get("class_models").get("associations")
  inhers = data.get("class_models").get("inheritances")

  if old_name != klass.name:
    for uc in ucs:
      events = uc.get("usecase_events")
      for event in events:
        steps = event.get("event_steps")
        for step in steps:
          if step.get("class_name") == old_name:
            step["class_name"] = klass.name
    
    for assoc in assocs:
      if assoc.get("src").get("class_name") == old_name:
        assoc.get("src")["class_name"] = klass.name
      if assoc.get("tgt").get("class_name") == old_name:
        assoc.get("tgt")["class_name"] = klass.name
    
    data.get("class_models")["relations"] = assocs
    
    for inher in inhers:
      if inher.get("parent_class_name") == old_name:
        inher["parent_class_name"] = klass.name
      if inher.get("child_class_name") == old_name:
        inher["child_class_name"] = klass.name

  data.get("class_models").get("classes")[cls_id] = klass.dict()
  jg.write_json(data)

@class_router.delete("/class/{cls_id}/")
def delete_class(cls_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  cls = data.get("class_models").get("classes").pop(cls_id)
  cls_name = cls.get("name")

  ucs = data.get("usecase_models").get("usecases")
  assocs = data.get("class_models").get("associations")
  inhers = data.get("class_models").get("inheritances")

  for uc in ucs:
    events = uc.get("usecase_events")
    for event in events:
      steps = event.get("event_steps")
      for step in steps:
        if step.get("class_name") == cls_name:
          step["class_name"] = None
  
  data.get("class_models")["associations"] = [assoc for assoc in assocs if assoc.get("src").get("class_name") != cls_name or assoc.get("tgt").get("class_name") != cls_name]
    
  data.get("class_models")["relations"] = assocs

  data.get("class_models")["inheritances"] = [inher for inher in inhers if inher.get("parent_class_name") != cls_name or inher.get("child_class_name") != cls_name]
  
  jg.write_json(data)

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
  return {"data": associations_by_class_name(class_name)}

def associations_by_class_name(class_name: str):
  jg = JsonGenerator()
  data = jg.return_data()

  associations = data.get("class_models").get("associations")
  class_associations = []

  for association in associations:
    if association.get("src").get("class_name") == class_name or association.get("tgt").get("class_name") == class_name:
      class_associations.append((associations.index(association), association))
  return class_associations

@class_router.post("/association/")
def create_association(assoc: Association):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("associations").append(assoc.dict())
  jg.write_json(data)

@class_router.put("/association/{asc_id}/")
def update_association(asc_id: int, assoc: Association):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("associations")[asc_id] = assoc.dict()
  jg.write_json(data)

@class_router.delete("/association/{asc_id}/")
def delete_association(asc_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("associations").pop(asc_id)
  jg.write_json(data)

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
  return {"data": inheritances_by_class_name(class_name)}

def inheritances_by_class_name(class_name: str) -> list[dict]:
  jg = JsonGenerator()
  data = jg.return_data()

  inheritances = data.get("class_models").get("inheritances")
  class_inheritances = []

  for inheritance in inheritances:
    if inheritance.get("parent_class_name") == class_name or inheritance.get("child_class_name") == class_name:
      class_inheritances.append((inheritances.index(inheritance), inheritance))
  return class_inheritances

@class_router.post("/inheritance/")
def create_inheritance(inher: Inheritance):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("inheritances").append(inher.dict())
  jg.write_json(data)

@class_router.put("/inheritance/{inh_id}/")
def update_inheritance(inh_id: int, inher: Inheritance):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("inheritances")[inh_id] = inher.dict()
  jg.write_json(data)

@class_router.delete("/inheritance/{inh_id}/")
def delete_inheritance(inh_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("inheritances").pop(inh_id)
  jg.write_json(data)

############
# Question #
############

@class_router.get("/questions/")
def get_class_questions() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()

  return {"data": data.get("class_models").get("questions")}

@class_router.post("/questions/")
def create_class_question(question: ClassQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("questions").append(question.dict())
  jg.write_json(data)

@class_router.put("/questions/{q_id}/")
def update_class_question(q_id: int, question: ClassQuestion):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("questions")[q_id] = question.dict()
  jg.write_json(data)

@class_router.delete("/questions/{q_id}/")
def delete_class_question(q_id: int):
  jg = JsonGenerator()
  data = jg.return_data()

  data.get("class_models").get("questions").pop(q_id)
  jg.write_json(data)