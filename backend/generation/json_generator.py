import json
import copy
import os
import datetime

from conversion.load_class import ClassLoader
from conversion.load_usecase import UsecaseLoader
from conversion.load_narrative import NarrativeLoader
from conversion.load_requirement import RequirementLoader
from conversion.load_actor import ActorLoader
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
    al = ActorLoader()

    narrative_data, narrative_q = nl.load()
    fr_data, nfr_data, br_data, requirements_q = rl.load()
    classes_data, associations_data, inheritances_data, classes_q = cl.load()
    usecases_data, usecases_q = ul.load()
    actor_data = al.load()

    data = {
      "narrative_models": {
        "domain_narrative": narrative_data.dict(),
        "questions": [nq.dict() for nq in narrative_q]
        },
      "requirement_models": {
        "functional_requirements": [fr.dict() for fr in fr_data],
        "non_functional_requirements": [nfr.dict() for nfr in nfr_data],
        "business_rules": [br.dict() for br in br_data],
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
      },
      "actors": [actor.dict() for actor in actor_data]
    }

    return data

  def save_data(self, data: dict, write_new=True):
    if write_new and os.path.exists("../out/out.json"):
      os.rename("../out/out.json", f"../out/out-old-since-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json")

    with open("../out/out.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4, ensure_ascii=False)

  def write_json(self, data: dict, write_new=False):
    try:
      valid_data = {
        "narrative_models": {
          "domain_narrative": pyd_req.DomainNarrative.model_validate(data.get("narrative_models").get("domain_narrative")).dict(),
          "questions": [pyd_q.NarrativeQuestion.model_validate(nq).dict() for nq in data.get("narrative_models").get("questions")]
          },
        "requirement_models": {
          "functional_requirements": [pyd_req.FunctionalRequirement.model_validate(fr).dict() for fr in data.get("requirement_models").get("functional_requirements")],
          "non_functional_requirements": [pyd_req.NonFunctionalRequirement.model_validate(nfr).dict() for nfr in data.get("requirement_models").get("non_functional_requirements")],
          "business_rules": [pyd_req.BusinessRule.model_validate(br).dict() for br in data.get("requirement_models").get("business_rules")],
          "questions": [pyd_q.RequirementQuestion.model_validate(rq).dict() for rq in data.get("requirement_models").get("questions")]
        },
        "class_models": {
          "classes": [pyd_cls.Class.model_validate(clazz).dict() for clazz in data.get("class_models").get("classes")],
          "associations": [pyd_cls.Association.model_validate(assoc).dict() for assoc in data.get("class_models").get("associations")],
          "relations": [pyd_cls.Association.model_validate(assoc).dict() for assoc in data.get("class_models").get("associations")],
          "inheritances": [pyd_cls.Inheritance.model_validate(inher).dict() for inher in data.get("class_models").get("inheritances")],
          "questions": [pyd_q.ClassQuestion.model_validate(cq).dict() for cq in data.get("class_models").get("questions")]
        },
        "usecase_models": {
          "usecases": [pyd_ucs.Usecase.model_validate(uc).dict() for uc in data.get("usecase_models").get("usecases")],
          "questions": [pyd_q.UsecaseQuestion.model_validate(uq).dict() for uq in data.get("usecase_models").get("questions")]
        },
        "actors": [pyd_req.Actor.model_validate(actor).dict() for actor in data.get("actors")]
      }

      self.save_data(valid_data, write_new=write_new)
    except Exception as e:
      print(f"INVALID DATA {e}: {data}")