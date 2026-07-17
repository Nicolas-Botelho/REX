import models.requirement as pyd
import models.question as pyd_q
from generation.json_reader import JsonReader

class RequirementLoader():
  def load(self):
    json_r = JsonReader()
    requirement_models = json_r.read().get("requirement_models")

    if requirement_models == None:
      return [], []

    return self.load_requirements(requirement_models.get("requirements")), self.load_questions(requirement_models.get("questions"))

  def load_requirements(self, models: list) -> list[pyd.Requirement]:
    requirements: list[pyd.Requirement] = []
    for req in models:
      try:
        requirements.append(pyd.Requirement.model_validate(req))
      except:
        print(f"INVALID REQUIREMENT {req}")
    return requirements
  
  def load_questions(self, models: list) -> list[pyd_q.Question]:
    questions: list[pyd_q.Question] = []
    for quest in models:
      try:
        questions.append(pyd_q.Question.model_validate(quest))
      except:
        print(f"INVALID QUESTION {quest}")
    return questions