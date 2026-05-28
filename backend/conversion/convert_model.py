from rex.serializers import json_serializers as json_ser
from ai_gen.models.klass import Class
# from ai_gen.models.usecase import Usecase, Step
import ai_gen.models.usecase as uc_mod

class ClassConverter():
  def load(self):
    models: list[Class] = []
    rd = json_ser.JsonClassSerializer()
    for clazz in rd.get():
      models.append(self.convert(clazz))
    return models

  def convert(self, model_dict):
    return Class.model_validate(model_dict)

class UsecaseConverter():
  def load(self):
    uc_models = []
    step_models = []
    uc_json = json_ser.JsonUseCaseSerializer()
    step_json = json_ser.JsonStepSerializer()
    for uc in uc_json.get():
      uc_models.append(self.convert_uc(uc))
    for step in step_json.get():
      step_model = self.convert_step(step)
      if step_model:
        step_models.append(step_model)

    return uc_models, step_models

  def convert_uc(self, model_dict):
    return uc_mod.Usecase.model_validate(model_dict)
  
  def convert_step(self, model_dict):
    print(model_dict)
    if "next_step" in model_dict:
      if "modification_type" in model_dict:
        return uc_mod.ModifyAction.model_validate(model_dict)
      elif "match_percent" in model_dict:
        return uc_mod.TextReadAction.model_validate(model_dict)
      else:
        return uc_mod.ReadAction.model_validate(model_dict)

    if "next_steps" in model_dict:
      return uc_mod.Decision.model_validate(model_dict)