import models.klass as pyd
import models.question as pyd_q
from generation.json_reader import JsonReader

class ClassLoader():
  def load(self):
    json_r = JsonReader()
    class_models = json_r.read().get("class_models")

    if class_models == None:
      return [], [], [], []

    return self.load_classes(class_models.get("classes")), self.load_associations(class_models.get("associations")), self.load_inheritances(class_models.get("inheritances")), self.load_questions(class_models.get("questions"))

  def load_classes(self, models: list) -> list[pyd.Class]:
    classes: list[pyd.Class] = []
    # rd = json_ser.JsonClassSerializer()
    for clazz in models:
      try:
        classes.append(pyd.Class.model_validate(clazz))
      except:
        print(f"INVALID CLASS {clazz}")
    return classes

  def load_associations(self, models: list) -> list[pyd.Association]:
    associations: list[pyd.Association] = []
    # rd = json_ser.JsonAssociationSerializer()
    for assoc in models:
      try:
        associations.append(pyd.Association.model_validate(assoc))
      except:
        print(f"INVALID ASSOCIATION {assoc}")
    return associations

  def load_inheritances(self, models: list) -> list[pyd.Inheritance]:
    inheritances: list[pyd.Inheritance] = []
    # rd = json_ser.JsonInheritanceSerializer()
    for inher in models:
      try:
        inheritances.append(pyd.Inheritance.model_validate(inher))
      except:
        print(f"INVALID INHERITANCE {inher}")
    return inheritances
  
  def load_questions(self, models: list) -> list[pyd_q.Question]:
    questions: list[pyd_q.Question] = []
    for quest in models:
      try:
        questions.append(pyd_q.Question.model_validate(quest))
      except:
        print(f"INVALID QUESTION {quest}")
    return questions