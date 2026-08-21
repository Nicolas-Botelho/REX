from generation.json_generator import JsonGenerator
from views.class_view import associations_by_class_name, inheritances_by_class_name

from fastapi import APIRouter

doc_router = APIRouter(prefix="/document")

@doc_router.get("/narrative/")
def narrative_md():
  jg = JsonGenerator()
  data = jg.return_data()

  nm: dict = data.get("narrative_models")

  return {'data': f"""# Domain Narrative
{nm.get("domain_narrative").get("narrative")}

# Questions
{print_questions(nm.get("questions"), mode="narrative")}"""}

@doc_router.get("/requirements/")
def requirements_md():
  jg = JsonGenerator()
  data = jg.return_data()

  rm: dict = data.get("requirement_models")

  return {'data': f"""# Functional Requirements (FRs)
{print_frs(rm.get("functional_requirements"))}

# Non Functional Requirements (NFRs)
{print_nfrs(rm.get("non_functional_requirements"))}

# Business Rules (BRs)
{print_brs(rm.get("business_rules"))}

# Questions
{print_questions(rm.get("questions"), mode="requirements")}"""}

def print_frs(frs: list):
  fr_string = ""

  for fr in frs:
    fr_string += f"## {fr.get("code")}\n\nObjective: {fr.get("objective")}\n\nDescription: {fr.get("description")}\n\n{fr.get("actor_name")}\n\nPriority: {fr.get("priority").name.lower()} do\n\n### **Depends on**\n\n{print_fr_req(fr.get("depends_on_requirements_codes"), fr.get("apply_business_rules_codes"))}\n\n"
  
  return fr_string

def print_fr_req(frs: list, brs: list):
  req_string = ""

  for fr in frs:
    req_string += f"* {fr}\n"
  for br in brs:
    req_string += f"* {br}\n"
  
  return req_string

def print_nfrs(nfrs: list):
  nfr_string = ""

  for nfr in nfrs:
    nfr_string += f"## {nfr.get("code")}\n\nDescription: {nfr.get("description")}\n\nCategory: {nfr.get("category").name.lower()}\n\nPriority: {nfr.get("priority").name.lower()} do\n\n### **Applied on**\n\n{print_nfr_req(nfr.get("applies_on_requirements_codes"))}\n\n"
  
  return nfr_string

def print_nfr_req(frs: list):
  req_string = ""

  for fr in frs:
    req_string += f"* {fr}\n"
  
  if req_string == "":
    req_string += "Whole system\n"
  
  return req_string

def print_brs(brs: list):
  br_string = ""

  for br in brs:
    br_string += f"## {br.get("code")}\n\n{br.get("description")}\n\n"
  
  return br_string

@doc_router.get("/usecase/")
def usecase_md():
  jg = JsonGenerator()
  data = jg.return_data()

  um = data.get("usecase_models")

  return {'data': f"""# Usecases
{print_ucs(um.get("usecases"))}

# Questions
{print_questions(um.get("questions"), mode="usecases")}"""}

def print_ucs(ucs: list):
  uc_string = ""

  for uc in ucs:
    uc_string += f"## {uc.get("name")}\n\n### Events\n\n{print_events(uc.get("usecase_events"))}"
  
  return uc_string

def print_events(events: list):
  event_string = ""

  for event in events:
    event_string += f"#### {event.get("name")}\n\nPerformed by: {"; ".join(event.get("actor_name")) if event.get("actor_name") else "No actor defined"}\n\nRelated to: {"; ".join(event.get("functional_requirements_codes")) if event.get("functional_requirements_codes") else ""}\n\nSteps:\n\n{print_steps(event.get("event_steps"))}"

  return event_string

def print_actors(actors: list):
  actor_string = ""

  for actor in actors:
    actor_string += f"{actor}; "

  return actor_string

def print_uc_req(frs: list):
  req_string = ""

  for fr in frs:
    req_string += f"* {fr}\n"
  
  return req_string

def print_steps(steps: list):
  step_string = "| Code | Description | Class Name | Category | Next Step |\n| --- | --- | --- | --- | --- |\n"

  for step in steps:
    step_string += f"| {step.get("step_code")} | {step.get("description")} | {step.get("class_name") if step.get("class_name") else ""} | {step.get("category").name.lower() if step.get("category") else "decision"} | {print_next_steps(step)}|\n"
  
  return step_string

def print_next_steps(step):
  if step.get("next_step"):
    return step.get("next_step")
  if step.get("next_steps"):
    return "; ".join(step.get("next_steps"))
  return ""

@doc_router.get("/class/")
def class_md():
  jg = JsonGenerator()
  data = jg.return_data()

  cm = data.get("class_models")

  return {'data': f"""# Classes
{print_cls(cm.get("classes"))}

# Question
{print_questions(cm.get("questions"), mode="classes")}"""}

def print_cls(classes: list):
  class_string = ""

  for cls in classes:
    class_string += f"## {cls.get("name")} {"<"+cls.get("stereotype")+">" if cls.get("stereotype") else ""}\n\n### Attributes\n\n{print_attributes(cls.get("class_attributes"))}\n\n### Associations\n\n{print_associations(associations_by_class_name(cls.get("name")))}\n\n### Inheritances\n\n{print_inheritances(inheritances_by_class_name(cls.get("name")))}"
  
  return class_string

def print_attributes(attrs: list):
  attr_string = ""

  for attr in attrs:
    attr_string += f"* {attr.get("name")}: {attr.get("attr_type").name.lower()} {"(many)" if attr.get("is_multiple") else ""} {"(valid values: " + ', '.join(attr.get("valid_values")) + ")" if attr.get("valid_values") else ""}\n"
  
  return attr_string

def print_associations(assocs: list):
  assoc_string = ""

  for assoc in assocs:
    src: dict = assoc[1].get("src")
    tgt: dict = assoc[1].get("tgt")

    assoc_string += f"* {src.get("class_name")} \"{src.get("class_min") if src.get("class_min") != None else "N"}..{src.get("class_max") if src.get("class_max") != None else "N"}\" --> \"{tgt.get("class_min") if tgt.get("class_min") != None else "N"}..{tgt.get("class_max") if tgt.get("class_max") != None else "N"}\" {tgt.get("class_name")}\n"

  return assoc_string

def print_inheritances(inhers: list):
  inher_string = ""

  for inher in inhers:

    inher_string += f"* {inher[1].get("parent_class_name")} <|-- {inher[1].get("child_class_name")}\n"

  return inher_string

def print_questions(questions: list, mode: str = ""):
  question_string = ""

  if mode == "narrative":
    for q in questions:
      question_string += f"{q.get("question")}\n\n"
  elif mode == "requirements":
    for q in questions:
      question_string += f"{q.get("question")} {"("+"; ".join(q.get("requirement_codes"))+")"}\n\n"
  elif mode == "usecases":
    for q in questions:
      question_string += f"{q.get("question")} {"("+"; ".join(q.get("usecase_names"))+")"}\n\n"
  elif mode == "classes":
    for q in questions:
      question_string += f"{q.get("question")} {"("+"; ".join(q.get("class_names"))+")"}\n\n"

  return question_string