import models.usecase as pyd
import models.question as pyd_q
from generation.json_reader import JsonReader

class UsecaseLoader():
  def __init__(self, project: int):
    self.project = project

  def load(self):
    try:
      filepath = JsonReader.read_projects()[self.project].get("filepath")
    except Exception as e:
      filepath = ""

    json_r = JsonReader(filepath)
    usecase_models = json_r.read().get("usecase_models")

    if usecase_models == None:
      return [], []

    return self.load_usecases(usecase_models.get("usecases")), self.load_questions(usecase_models.get("questions"))

  def load_usecases(self, models: list) -> list[pyd.Usecase]:
    usecases: list[pyd.Usecase] = []
    for uc in models:
      try:
        usecases.append(pyd.Usecase.model_validate(uc))
      except Exception as e:
        print(f"INVALID USECASE {e}: {uc}")
    return usecases

  def load_questions(self, models: list) -> list[pyd_q.UsecaseQuestion]:
    questions: list[pyd_q.UsecaseQuestion] = []
    for quest in models:
      try:
        questions.append(pyd_q.UsecaseQuestion.model_validate(quest))
      except Exception as e:
        print(f"INVALID QUESTION {e}: {quest}")
    return questions