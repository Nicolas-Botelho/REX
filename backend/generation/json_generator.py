import json

from ai_gen.models.response_model.class_response import ClassOutput
from ai_gen.models.response_model.usecase_response import UsecaseOutput
from conversion.convert_class import ClassConverter
from conversion.convert_usecase import UsecaseConverter

class JsonGenerator():
  def create(self):
    cc = ClassConverter()
    uc = UsecaseConverter()

    classes_data = cc.load().model_dump()
    usecases_data = uc.load().model_dump()

    data = {
      'class_models' : classes_data,
      'usecase_models' : usecases_data
    }

    with open("out/output.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)

    return True

  def read(self):
    pass