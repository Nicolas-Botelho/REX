from ai_gen.graph.usecase_class_graph import full_graph, ns_graph
from models.response_model.class_response import ClassOutput, HumanClassOutput
from models.response_model.usecase_response import UsecaseOutput
from models.response_model.requirement_response import RequirementOutput
from models.response_model.narrative_response import NarrativeOutput
from conversion.load_class import ClassLoader
from conversion.load_usecase import UsecaseLoader
from conversion.load_requirement import RequirementLoader
from conversion.load_narrative import NarrativeLoader
from conversion.load_actor import ActorLoader
from conversion.utils.transformation import TransformAssociation
from generation.json_generator import JsonGenerator

from fastapi import APIRouter, Body
from typing import Annotated

gen_router = APIRouter(prefix="/ai")

@gen_router.post("/run_all/")
def ai_view(input_text: Annotated[str, Body(embed=True)], overwrite: bool = False) -> dict:
  cl = ClassLoader()
  ul = UsecaseLoader()
  rl = RequirementLoader()
  nl = NarrativeLoader()
  al = ActorLoader()

  loaded_classes, loaded_assocs, loaded_inhers, loaded_class_q = cl.load()
  transformed_assocs = TransformAssociation.transform(loaded_assocs)
  clsInput = ClassOutput(classes=loaded_classes, associations=transformed_assocs, inheritances=loaded_inhers, questions=loaded_class_q)

  loaded_actors = al.load()

  loaded_usecases, loaded_usecase_q = ul.load()
  ucInput = UsecaseOutput(usecases=loaded_usecases, actors=loaded_actors, questions=loaded_usecase_q)

  loaded_frs, loaded_nfrs, loaded_brs, loaded_requirement_q = rl.load()
  rqInput = RequirementOutput(functional_requirements=loaded_frs, non_functional_requirements=loaded_nfrs, business_rules=loaded_brs, actors=loaded_actors, quesitons=loaded_requirement_q)

  loaded_narrative, loaded_narrative_q = nl.load()
  ndInput = NarrativeOutput(domain_narrative=loaded_narrative, questions=loaded_narrative_q)

  result = full_graph.invoke({'InputText': input_text, 'OldDomainNarrative': ndInput, 'OldRequirements': rqInput, 'OldUsecases': ucInput, 'OldClasses': clsInput})

  # print("NO STRUCT TEST START")
  # print(ns_graph.invoke({'InputText': input_text}))
  # print("NO STRUCT TEST END")

  new_classes: ClassOutput = result.get('Classes')
  new_usecases: UsecaseOutput = result.get('Usecases')
  new_requirements: RequirementOutput = result.get('Requirements')
  new_narrative: NarrativeOutput = result.get('DomainNarrative')

  if new_classes or new_usecases or new_requirements or new_narrative:
    jg = JsonGenerator()
    data = {
      "narrative_models": {
        "domain_narrative": new_narrative.domain_narrative.dict(),
        "questions": [nq.dict() for nq in new_narrative.questions]
      },
      "requirement_models": {
        "functional_requirements": [fr.dict() for fr in new_requirements.functional_requirements],
        "non_functional_requirements": [nfr.dict() for nfr in new_requirements.non_functional_requirements],
        "business_rules": [br.dict() for br in new_requirements.business_rules],
        "questions": [rq.dict() for rq in new_requirements.questions]
      },
      "class_models": {
        "classes": [clazz.dict() for clazz in new_classes.classes],
        "associations": [assoc.dict() for assoc in TransformAssociation.reverse(new_classes.associations)],
        "relations": [assoc.dict() for assoc in TransformAssociation.reverse(new_classes.associations)],
        "inheritances": [inher.dict() for inher in new_classes.inheritances],
        "questions": [cq.dict() for cq in new_classes.questions]
      },
      "usecase_models": {
        "usecases": [uc.dict() for uc in new_usecases.usecases],
        "questions": [uq.dict() for uq in new_usecases.questions]
      },
      "actors": [actor.dict() for actor in new_requirements.actors]
    }
    jg.write_json(data, write_new=not overwrite)
    
  return {}