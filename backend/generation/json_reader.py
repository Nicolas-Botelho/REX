class JsonReader():
  def read(self):
    pass

  # def read(self, data: dict[str, dict[str, Any]]):
  #   class_models = data.get("class_models")
  #   usecase_models = data.get("usecase_models")
  #   co = ClassOutput()
  #   uo = UsecaseOutput()
  #   cc = ClassConverter()
  #   uc = UsecaseConverter()

  #   if class_models:
  #     enums = class_models.get("enums")
  #     classes = class_models.get("classes")
  #     relations = class_models.get("relations")
      
  #   if usecase_models:
  #     self._usecase_read(usecase_models)
  
  # def _class_read(self, data: dict[str, dict[str, Any]], cout: ClassOutput) -> bool:
  #   name = data.get("name")

  #   # create class

  #   klass_attributes = data.get("klass_attributes")
  #   for attribute in klass_attributes:
  #     if attribute.get("enum"):
  #       self._enum_attribute_read(attribute)
  #     elif attribute.get("attr_type"):
  #       self._prim_attribute_read(attribute)

  # def _usecase_read(data: dict[str, dict[str, Any]]):
  #   pass