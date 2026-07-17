import models.requirement as pyd
import models.question as pyd_q
from generation.json_reader import JsonReader

class NarrativeLoader():
  def load(self):
    json_r = JsonReader()
    narrative_models = json_r.read().get("narrative_models")

    if narrative_models == None:
      return pyd.DomainNarrative(system_context="", users=[], system_functionalities=[]), []

    return self.load_narrative(narrative_models.get("domain_narrative")), self.load_questions(narrative_models.get("questions"))

  def load_narrative(self, model: dict) -> pyd.DomainNarrative | None:
    try:
      return pyd.DomainNarrative.model_validate(model)
    except:
      print(f"INVALID NARRATIVE {model}")
      return None
  
  def load_questions(self, models: list) -> list[pyd_q.Question]:
    questions: list[pyd_q.Question] = []
    for quest in models:
      try:
        questions.append(pyd_q.Question.model_validate(quest))
      except:
        print(f"INVALID QUESTION {quest}")
    return questions