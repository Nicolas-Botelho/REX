import json
import copy
import os
import datetime

from conversion.load_class import ClassLoader
from conversion.load_usecase import UsecaseLoader
from conversion.load_narrative import NarrativeLoader
from conversion.load_requirement import RequirementLoader
import models.klass as pyd_cls
import models.usecase as pyd_ucs
import models.requirement as pyd_req
import models.question as pyd_q

class JsonGenerator():
  def return_data(self):
    cl = ClassLoader()
    ul = UsecaseLoader()
    rl = RequirementLoader()
    nl = NarrativeLoader()

    narrative_data, narrative_q = nl.load()
    requirement_data, requirements_q = rl.load()
    classes_data, associations_data, inheritances_data, classes_q = cl.load()
    usecases_data, usecases_q = ul.load()

    data = {
      "narrative_models": {
        "domain_narrative": narrative_data.dict(),
        "questions": [nq.dict() for nq in narrative_q]
        },
      "requirement_models": {
        "requirements": [requi.dict() for requi in requirement_data],
        "questions": [rq.dict() for rq in requirements_q]
      },
      "class_models": {
        "classes": [clazz.dict() for clazz in classes_data],
        "associations": [assoc.dict() for assoc in associations_data],
        "relations": [assoc.dict() for assoc in associations_data],
        "inheritances": [inher.dict() for inher in inheritances_data],
        "questions": [cq.dict() for cq in classes_q]
      },
      "usecase_models": {
        "usecases": [usecs.dict() for usecs in usecases_data],
        "questions": [uq.dict() for uq in usecases_q]
      }
    }

    return data

  def write_json(self,
  classes: list[pyd_cls.Class], associations: list[pyd_cls.Association], inheritances: list[pyd_cls.Inheritance], classes_questions: list[pyd_q.Question],
  usecases: list[pyd_ucs.Usecase], usecases_questions: list[pyd_q.Question],
  requirements: list[pyd_req.Requirement], requirement_questions: list[pyd_q.Question],
  domain_narrative: pyd_req.DomainNarrative, narrative_questions: list[pyd_q.Question],
  write_new=True):
    data = {
      "narrative_models": {
        "domain_narrative": domain_narrative.dict(),
        "questions": [nq.dict() for nq in narrative_questions]
        },
      "requirement_models": {
        "requirements": [requi.dict() for requi in requirements],
        "questions": [rq.dict() for rq in requirement_questions]
      },
      "class_models": {
        "classes": [clazz.dict() for clazz in classes],
        "associations": [assoc.dict() for assoc in associations],
        "relations": [assoc.dict() for assoc in associations],
        "inheritances": [inher.dict() for inher in inheritances],
        "questions": [cq.dict() for cq in classes_questions]
      },
      "usecase_models": {
        "usecases": [usecs.dict() for usecs in usecases],
        "questions": [uq.dict() for uq in usecases_questions]
      }
    }

    if write_new and os.path.exists("../out/out.json"):
      os.rename("../out/out.json", f"../out/out-old-since-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json")

    with open("../out/out.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4, ensure_ascii=False)