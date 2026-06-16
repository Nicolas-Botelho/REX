import ai_gen.models.usecase as pyd
import rex.models.usecase as djg
from rex.serializers import json_serializers as json_ser

class UsecaseLoader():
  def load(self):
    return self.load_usecases()

  def load_usecases(self) -> list[pyd.Usecase]:
    usecases: list[pyd.Usecase] = []
    rd = json_ser.JsonUseCaseSerializer()
    for uc in rd.get():
      for event in uc["usecase_events"]:
        for step in event["event_steps"]:
          step["class_name"] = step["clazz"]["name"]
          if step.get("next_step"):
            step["next_step"] = step["next_step"]["step_code"]
          if step.get("next_steps"):
            step["next_steps"] = [ns["step_code"] for ns in step["next_steps"]]
      
      usecases.append(pyd.Usecase.model_validate(uc))

    return usecases