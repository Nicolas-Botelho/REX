from ai_gen.state import State
from ai_gen.llm import llm
from ai_gen.response_model.requirement_response import FROutput
from ai_gen.models.requirements import FunctionalRequirement

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage

def call_llm(state: State):
  print('FR Agent Start')

  input_text = state.get('InputText')

  llm_struct_output = llm.with_structured_output(FROutput)

  example_output = FROutput(fr_list=[
    FunctionalRequirement(
      iD=1,
      description='FR01 description',
      testCase=[1],
      epics=[1]
    ),
  ])

  instruction = f'''
  # Task
  You are a Requirements Engineer tasked with extracting the functional requirements (FR) of a given text about a system.

  ## About the Requirements
  - Only extract explicit and implied requirements of the text, do not create any other requirements.
  - Use the Requirements Engineering techniques to identify the requirements of the text, even when there are more than one requirement in the same part of the text (e.g.: "The system should allow user registration by the Admin." means there is a User CRUD and some sort of Admin Login (implied, except if the text explicitly say something else about it in another moment)).
  - Explicit requirements have priority compared to implied ones. This means that if a explicit requirement contradicts a implied requirement, you should keep the explicit requirement.

  ## About the Structured Output Format for Functional Requirements (FR)
  {example_output.model_dump_json()}

  ## Final Instructions
  - Answer strictly in the Structured Output Format;
  - If any FRs are given, answer only with the new requirements, do not repeat given requirements; and
  - Answer in the same language the given text in writen.
  '''

  current_fr = state.get('OldFunctionalRequirements')
  current_fr_text = ''
  if current_fr:
    current_fr_text = f'''
  ## Current Functional Requirements
  Also, use the following FRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement contradict one of this requirements, change the new requirement.

  ### Functional Requirements
  {current_fr.__str__()}
  '''
  current_nfr = state.get('OldNonFunctionalRequirements')
  current_nfr_text = ''
  if current_nfr:
    current_nfr_text = f'''
  ## Current Non Functional Requirements
  Also, use the following NFRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement contradict one of this requirements, change the new requirement.

  ### Non Functional Requirements
  {current_nfr.__str__()}
  '''
  current_br = state.get('OldBusinessRules')
  current_br_text = ''
  if current_br:
    current_br_text = f'''
  ## Current Business Requirements
  Also, use the following BRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement contradict one of this requirements, change the new requirement.

  ### Business Rules
  {current_br.__str__()}
  '''

  llm_input = [SystemMessage(content=instruction+current_fr_text+current_nfr_text+current_br_text), HumanMessage(content=input_text)]

  # supposedly, the response type should be the same of the structured output
  response = llm_struct_output.invoke(llm_input)
  # print(response.fr_list)

  print('FR Agent End')
  return {**state, 'FunctionalRequirements': response.fr_list}