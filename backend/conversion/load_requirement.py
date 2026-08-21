import models.requirement as pyd
import models.question as pyd_q
from generation.json_reader import JsonReader

class RequirementLoader():
  def load(self):
    json_r = JsonReader()
    requirement_models = json_r.read().get("requirement_models")

    if requirement_models == None:
      return [], [], [], []

    return self.load_frs(requirement_models.get("functional_requirements")), self.load_nfrs(requirement_models.get("non_functional_requirements")), self.load_brs(requirement_models.get("business_rules")), self.load_questions(requirement_models.get("questions"))

  def load_frs(self, models: list) -> list[pyd.FunctionalRequirement]:
    frs: list[pyd.FunctionalRequirement] = []
    for model in models:
      try:
        frs.append(pyd.FunctionalRequirement.model_validate(model))
      except Exception as e:
        print(f"INVALID REQUIREMENT {e}: {model}")
    return frs
  
  def load_nfrs(self, models: list) -> list[pyd.NonFunctionalRequirement]:
    nfrs: list[pyd.NonFunctionalRequirement] = []
    for model in models:
      try:
        nfrs.append(pyd.NonFunctionalRequirement.model_validate(model))
      except Exception as e:
        print(f"INVALID REQUIREMENT {e}: {model}")
    return nfrs

  def load_brs(self, models: list) -> list[pyd.BusinessRule]:
    brs: list[pyd.BusinessRule] = []
    for model in models:
      try:
        brs.append(pyd.BusinessRule.model_validate(model))
      except Exception as e:
        print(f"INVALID REQUIREMENT {e}: {model}")
    return brs

  def load_questions(self, models: list) -> list[pyd_q.RequirementQuestion]:
    questions: list[pyd_q.RequirementQuestion] = []
    for quest in models:
      try:
        questions.append(pyd_q.RequirementQuestion.model_validate(quest))
      except Exception as e:
        print(f"INVALID QUESTION {e}: {quest}")
    return questions