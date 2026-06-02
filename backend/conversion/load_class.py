import ai_gen.models.klass as pyd
import rex.models.klass as djg
from rex.serializers import json_serializers as json_ser

class ClassLoader():
  def load(self):
    return self.load_classes(), self.load_associations(), self.load_inheritances()

  def load_classes(self) -> list[pyd.Class]:
    classes: list[pyd.Class] = []
    rd = json_ser.JsonClassSerializer()
    for clazz in rd.get():
      classes.append(pyd.Class.model_validate(clazz))
    return classes

  def load_associations(self) -> list[pyd.Association]:
    associations: list[pyd.Association] = []
    rd = json_ser.JsonAssociationSerializer()
    for assoc in rd.get():
      associations.append(pyd.Association.model_validate(assoc))
    return associations

  def load_inheritances(self) -> list[pyd.Inheritance]:
    inheritances: list[pyd.Inheritance] = []
    rd = json_ser.JsonInheritanceSerializer()
    for inher in rd.get():
      inheritances.append(pyd.Inheritance.model_validate(inher))
    return inheritances