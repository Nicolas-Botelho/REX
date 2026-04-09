import json
import copy
from typing import Any

from conversion.convert_class import ClassConverter
from conversion.convert_usecase import UsecaseConverter
from generation.utils import enum_labels

class JsonGenerator():
  def create(self):
    cc = ClassConverter()
    uc = UsecaseConverter()

    classes_data = cc.load().model_dump()
    usecases_data = uc.load().model_dump()

    data = self.nest_data({
      'class_models' : classes_data,
      'usecase_models' : usecases_data
    })

    with open("../out/output.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)

    return True

  def nest(self, elem: dict, reverse_ref_elem_list: list[dict], ref_name: str, lookup_name: str, nest_name: str, many: bool = True):
    """
    Nest a element in a object inside a list.
    OBS: The lookup_name must be unique, otherwise the method will change only one of the dicts.

    Args:
      elem (dict): element to be nested.
      reverse_ref_elem_list (list[dict]): list with the dict that the element will be nested inside of.
      ref_name (str): name of the reference key in elem. Must reference a unique field.
      lookup_name (str): name of the lookup key in the target dict. Must be unique.
      nest_name (str): name of the key that the elem will be nested into.
      many (bool): if true, the nest field will be considered as a list; else, it will be considered a single value field and will uptade its value, if the field already exists.

    Returns:
      None: changes the correct dict inside the list.
    """

    reference = elem.get(ref_name)
    reverse_ref_map = {}
    for item in reverse_ref_elem_list:
      key = item.get(lookup_name)
      if type(key) != dict:
        reverse_ref_map[key] = item
    reverse_ref_elem = reverse_ref_map.get(reference)

    if reverse_ref_elem is None:
      raise Exception(f"Invalid reference: {ref_name}={reference}")

    if many:
      reverse_ref_elem.setdefault(nest_name, []).append(copy.copy(elem))
    else:
      reverse_ref_elem[nest_name] = copy.copy(elem)

  def nest_data(self, data: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:

    # nested structure: classes
    # class
    #   class prim attr
    #   class enum attr
    # enum
    #   enum attr
    # relation
    #   rcr

    # nested structure: usecases
    # usecase
    #   event
    #     actor
    #     step

    class_models = data.get('class_models')
    usecase_models = data.get('usecase_models')

    enum_list = class_models.get('enums')
    enum_attr_list = class_models.get('enum_attributes')
    class_list = class_models.get('classes')
    class_enum_attr_list = class_models.get('class_enum_attributes')
    class_primitive_attr_list = class_models.get('class_primitive_attributes')
    relation_class_ref_list = class_models.get('relation_class_references')
    relation_list = class_models.get('relations')

    actor_list = usecase_models.get('actors')
    event_list = usecase_models.get('usecase_events')
    step_list = usecase_models.get('events_steps')
    usecase_list = usecase_models.get('usecases')

    # enum attributes into enum
    for elem in enum_attr_list:
      elem['label'] = enum_labels(elem.get('value'))
      self.nest(elem, enum_list, 'enum', 'iD', 'enum_attributes')
    class_models.pop('enum_attributes')

    # class attributes into class
    for elem in class_enum_attr_list:
      self.nest(elem, class_list, 'klass', 'iD', 'klass_attributes')
    last_enum_attr_id = class_enum_attr_list[-1].get('iD')
    class_models.pop('class_enum_attributes')

    # class attributes into class
    for elem in class_primitive_attr_list:
      elem['iD'] = elem.get('iD') + last_enum_attr_id
      self.nest(elem, class_list, 'klass', 'iD', 'klass_attributes')
    class_models.pop('class_primitive_attributes')

    # references into relation
    for elem in relation_class_ref_list:
      # compare rcr iD with relation src
      try:
        self.nest(elem, relation_list, 'iD', 'src', 'src', many=False)
      except:
        pass
      # compare rcr iD with relation tgt
      try:
        self.nest(elem, relation_list, 'iD', 'tgt', 'tgt', many=False)
      except:
        pass
    class_models.pop('relation_class_references')
    
    # steps into event
    for elem in step_list:
      self.nest(elem, event_list, 'event', 'iD', 'event_steps')
    usecase_models.pop('events_steps')

    # actors into event
    for elem in actor_list:
      # compare actor iD with event actor
      self.nest(elem, event_list, 'iD', 'actor', 'actor', many=False)
    usecase_models.pop('actors')

    # events into usecase
    for elem in event_list:
      self.nest(elem, usecase_list, 'usecase', 'iD', 'usecase_events')
    usecase_models.pop('usecase_events')

    return data