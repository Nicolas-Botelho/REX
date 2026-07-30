from ai_gen.graph.usecase_class_graph import full_graph, ns_graph
from models.response_model.class_response import ClassOutput, HumanClassOutput
from models.response_model.usecase_response import UsecaseOutput
from models.response_model.requirement_response import RequirementOutput
from models.response_model.narrative_response import NarrativeOutput
from conversion.load_class import ClassLoader
from conversion.load_usecase import UsecaseLoader
from conversion.load_requirement import RequirementLoader
from conversion.load_narrative import NarrativeLoader
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

  loaded_classes, loaded_assocs, loaded_inhers, loaded_class_q = cl.load()
  transformed_assocs = TransformAssociation.transform(loaded_assocs)
  clsInput = ClassOutput(classes=loaded_classes, associations=transformed_assocs, inheritances=loaded_inhers, questions=loaded_class_q)

  loaded_usecases, loaded_usecase_q = ul.load()
  ucInput = UsecaseOutput(usecases=loaded_usecases, questions=loaded_usecase_q)

  loaded_requirements, loaded_requirement_q = rl.load()
  rqInput = RequirementOutput(requirements=loaded_requirements, questions=loaded_requirement_q)

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
    jg.write_json(new_classes.classes, TransformAssociation.reverse(new_classes.associations), new_classes.inheritances, new_classes.questions,
    new_usecases.usecases, new_usecases.questions,
    new_requirements.requirements, new_requirements.questions,
    new_narrative.domain_narrative, new_narrative.questions, write_new=not overwrite)
    
  return {}