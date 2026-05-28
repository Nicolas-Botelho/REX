import json
import copy

import ai_gen.models.klass as cls_mod
import ai_gen.models.usecase as uc_mod
from conversion.convert_model import ClassConverter, UsecaseConverter
from generation.utils import enum_labels

class JsonGenerator():
  def create(self):
    cc = ClassConverter()
    uc = UsecaseConverter()

    classes_data = cc.load()
    usecases_data, step_data = uc.load()
    data = {
      "class_models": {
        "enums": [],
        "classes": [],
        "relations": [],
        "inheritances": []
      },
      "usecase_models": {
        "usecases": [],
        "actors": [],
        "steps": []
      }
    }

    data["class_models"] = self.fill_classes(classes_data)
    data["usecase_models"] = self.fill_usecases(usecases_data, step_data)

    with open("../out/out.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)

    return True
  
  def fill_classes(self, cls_list: list[cls_mod.Class]):
    data = {
      "enums": [],
      "classes": [],
      "relations": [],
      "inheritances": []
    }

    for cls in cls_list:
      new_class = {
        "id": cls.id,
        "name": cls.name,
        "klass_attributes": [] 
      }

      for atr in cls.class_attrs:
        new_attr = None
        if isinstance(atr, cls_mod.ClassAttributePrim):
          new_attr = {
            "id": atr.id,
            "name": atr.name,
            "attr_type": atr.attr_type,
            "klass": atr.klass
          }
        elif isinstance(atr, cls_mod.ClassAttributeEnum):
          new_attr = {
            "id": atr.id,
            "name": atr.name,
            "enum": atr.enum.id,
            "klass": atr.klass
          }
          new_enum = {
            "id": atr.enum.id,
            "name": atr.enum.name,
            "enum_attributes": [{"id": value.id, "value":value.value, "label":enum_labels(value.value), "enum":value.enum.id} for value in atr.enum.enum_values]
          }
          if not any(x["id"] == new_enum["id"] for x in data["enums"]):
            data["enums"].append(new_enum)

        if new_attr:
          new_class["klass_attributes"].append(copy.deepcopy(new_attr))

      for rel in cls.class_relations:
        new_rel = None
        if rel.rcr_as_src:
          new_rel = {
            "id": rel.rcr_as_src.id,
            "src": {
              "id": rel.id,
              "minim": rel.minim,
              "maxim": rel.maxim,
              "ref_class": rel.ref_class.id
            },
            "tgt": {
              "id": rel.rcr_as_src.tgt.id,
              "minim": rel.rcr_as_src.tgt.minim,
              "maxim": rel.rcr_as_src.tgt.maxim,
              "ref_class": rel.rcr_as_src.tgt.ref_class.id
            }
          }
        elif rel.rcr_as_tgt:
          new_rel = {
            "id": rel.rcr_as_tgt.id,
            "src": {
              "id": rel.rcr_as_tgt.src.id,
              "minim": rel.rcr_as_tgt.src.minim,
              "maxim": rel.rcr_as_tgt.src.maxim,
              "ref_class": rel.rcr_as_tgt.src.ref_class.id
            },
            "tgt": {
              "id": rel.id,
              "minim": rel.minim,
              "maxim": rel.maxim,
              "ref_class": rel.ref_class.id
            }
          }
        if new_rel and not any(x["id"] == new_rel["id"] for x in data["relations"]):
          data["relations"].append(new_rel)

      for inh in cls.class_childs:
        new_inh = {
          "id": inh.id,
          "parent_class": inh.parent.id,
          "child_class": inh.child.id
        }
        if not any(x["id"] == new_inh["id"] for x in data["inheritances"]):
          data["inheritances"].append(new_inh)
      for inh in cls.class_parents:
        new_inh = {
          "id": inh.id,
          "parent_class": inh.parent.id,
          "child_class": inh.child.id
        }
        if not any(x["id"] == new_inh["id"] for x in data["inheritances"]):
          data["inheritances"].append(new_inh)
      
      data["classes"].append(copy.deepcopy(new_class))

    return data

  def fill_usecases(self, uc_list: list[uc_mod.Usecase], st_list: list[uc_mod.Step]):
    data = {
      "usecases": [],
      "actors": [],
      "steps": []
    }

    for uc in uc_list:
      new_uc = {
        "id": uc.id,
        "name": uc.name,
        "usecase_events": []
      }

      for event in uc.usecase_events:
        new_actor = {
          "id": event.actor.id,
          "name": event.actor.name,
          "description": event.actor.description
        }
        if not any(x["id"] == new_actor["id"] for x in data["actors"]):
          data["actors"].append(copy.deepcopy(new_actor))

        new_step = self.action_dict(event.first_step)
        if not any(x["id"] == new_step["id"] for x in data["steps"]):
          data["steps"].append(copy.deepcopy(new_step))

        new_event = {
          "id": event.id,
          "name": event.name,
          "actor": event.actor.id,
          "first_step": event.first_step.id
        }
        new_uc["usecase_events"].append(copy.deepcopy(new_event))

      data["usecases"].append(copy.deepcopy(new_uc))

    for step in st_list:
      new_step = None
      if isinstance(step, uc_mod.Action):
        new_step = self.action_dict(step)
      elif isinstance(step, uc_mod.Decision):
        new_step = {
          "id": step.id,
          "description": step.description,
          "next_steps": [next_step_id for next_step_id in step.next_steps]
        }
      if new_step and not any(x["id"] == new_step["id"] for x in data["steps"]):
        data["steps"].append(new_step)
    
    return data

  def action_dict(self, action: uc_mod.Action):
    if isinstance(action, uc_mod.ModifyAction):
      if action.action_type == 'create':
        return {
          "id": action.id,
          "action_type": "CREATE_ACTION",
          "description": action.description,
          "next_step": action.next_step,
          "related_klasses": [klass.id for klass in action.related_classes]
        }
      elif action.action_type == 'update':
        return {
          "id": action.id,
          "action_type": "UPDATE_ACTION",
          "description": action.description,
          "next_step": action.next_step,
          "related_klasses": [klass.id for klass in action.related_classes]
        }
      elif action.action_type == 'delete':
        return {
          "id": action.id,
          "action_type": "CREATE_ACTION",
          "description": action.description,
          "next_step": action.next_step,
          "related_klasses": [klass.id for klass in action.related_classes]
        }
    elif isinstance(action, uc_mod.TextReadAction):
      return {
        "id": action.id,
        "action_type": "READ_ACTION",
        "match_percent": action.match_percent,
        "description": action.description,
        "next_step": action.next_step,
        "related_klasses": [klass.id for klass in action.related_classes],
        "related_attributes": [attr.id for attr in action.read_attributes]
      }
    elif isinstance(action, uc_mod.ReadAction):
      return {
        "id": action.id,
        "action_type": "READ_ACTION",
        "description": action.description,
        "next_step": action.next_step,
        "related_klasses": [klass.id for klass in action.related_classes],
        "related_attributes": [attr.id for attr in action.read_attributes]
      }
    else:
      return {
        "id": action.id,
        "action_type": "NO_TYPE_ACTION",
        "description": action.description,
        "next_step": action.next_step
      }