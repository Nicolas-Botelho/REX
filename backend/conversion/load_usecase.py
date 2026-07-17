import models.usecase as pyd
import models.question as pyd_q
from generation.json_reader import JsonReader


class UsecaseLoader():
  def load(self):
    json_r = JsonReader()
    usecase_models = json_r.read().get("usecase_models")

    if usecase_models == None:
      return [], []

    return self.load_usecases(usecase_models.get("usecases")), self.load_questions(usecase_models.get("questions"))

  def load_usecases(self, models: list) -> list[pyd.Usecase]:
    usecases: list[pyd.Usecase] = []
    # rd = json_ser.JsonUseCaseSerializer()
    for uc in models:
      # for event in uc["usecase_events"]:
      #   for step in event["event_steps"]:
      #     step["class_name"] = step["clazz"]["name"]
      #     if step.get("next_step"):
      #       step["next_step"] = step["next_step"]["step_code"]
      #     if step.get("next_steps"):
      #       step["next_steps"] = [ns["step_code"] for ns in step["next_steps"]]
      try:
        usecases.append(pyd.Usecase.model_validate(uc))
      except:
        print(f"INVALID USECASE {uc}")
    return usecases

  def load_questions(self, models: list) -> list[pyd_q.Question]:
    questions: list[pyd_q.Question] = []
    for quest in models:
      try:
        questions.append(pyd_q.Question.model_validate(quest))
      except:
        print(f"INVALID QUESTION {quest}")
    return questions