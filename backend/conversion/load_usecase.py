import ai_gen.models.usecase as pyd
import rex.models.usecase as djg
from rex.serializers import json_serializers as json_ser

class UsecaseLoader():
  def load(self):
    return self.load_usecases()

  def load_usecases(self):
    usecases: list[pyd.Usecase] = []
    rd = json_ser.JsonUseCaseSerializer()
    for uc in rd.get():
      usecases.append(pyd.Usecase.model_validate(uc))
    return usecases