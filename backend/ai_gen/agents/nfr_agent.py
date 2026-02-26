from backend.ai_gen.state import State
from backend.ai_gen.llm import llm
from backend.ai_gen.response_model.requirement_response import NFROutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage

def call_llm(state: State):
  print('NFR Agent Start')

  input_text = state.get('InputText')
  new_fr = state.get('FunctionalRequirements')

  llm_struct_output = llm.with_structured_output(NFROutput)

  instruction = f'''
  # Task
  You are a Requirements Engineer tasked with extracting the non functional requirements (NFR) of a given text about a system and given the functional requirements (FR) of that system.

  ## About the Requirements
  - Only extract explicit and implied requirements of the text, do not create any other requirements.
  - Use the Requirements Engineering techniques to identify the requirements of the text, even when there are more than one requirement in the same part of the text (e.g.: "The system should allow user registration by the Admin only until 6 PM." means there is, beside the FR, a NFR saying that the system only allow new registrations until 6 PM.
  - Explicit requirements have priority compared to implied ones. This means that if a explicit requirement contradicts a implied requirement, you should keep the explicit requirement.

  ## About the Structured Output Format for Non Functional Requirements (NFR)
  A NFR have the following parts:
  - iD: A unique integer identification of the NFR;
  - priority: A integer value that defines the priority level of a requirement. It must be inside the values defined in the limits;
  - limits: A object with a min value and a max value. Defines the range of the priority that a FR can assume;
  - description: A textual description of the requirement; and
  - affectedFR: A list of all the FRs that are affected by that NFR.

  ### Abstract Classes
  Reading the Structured Output Format you may find some classes named in the following pattern '_SOME_NAME_HERE'. This (starting with underscore) means that the class is abstract, therefore if must not be instanciated in a object by its own, the instance must be of a classe that inherits it. Whenever this is the case, the classes that can be instanciated, in the place of the abstract one, are stated above.

  ## Final Instructions
  - Answer strictly in the Structured Output Format; and
  - Answer in the same language the given text in writen.
  '''

  # current_fr = state.get('OldFunctionalRequirements')
  # current_fr_text = ''
  # if current_fr:
  #   current_fr_text = f'''
  # ## Current Functional Requirements
  # Also, use the following FRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement contradict one of this requirements, change the new requirement.

  # ### Functional Requirements
  # {current_fr.__str__()}
  # '''
  current_nfr = state.get('OldNonFunctionalRequirements')
  current_nfr_text = ''
  if current_nfr:
    current_nfr_text = f'''
  ## Current Non Functional Requirements (NFR)
  Also, use the following NFRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement contradict one of this requirements, change the new requirement.

  ### Non Functional Requirements
  {current_nfr.__str__()}
  '''
  current_br = state.get('OldBusinessRules')
  current_br_text = ''
  if current_br:
    current_br_text = f'''
  ## Current Business Rules (BR)
  Also, use the following BRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement contradict one of this requirements, change the new requirement.

  ### Business Rules
  {current_br.__str__()}
  '''
    
  new_fr_text = ''
  if new_fr:
    new_fr_text = f'''
  ## New Functional Requirements (FR)
  This are the new FRs. Consider that this given requirements are 100% correct, so do not exclude or modify them. If a new requirement, created by you, contradict one of this requirements, change the new requirement, that is, the one that you created.

  ### Functional Requirements
  {new_fr.__str__}
  '''

  llm_input = [SystemMessage(content=instruction+current_nfr_text+current_br_text), HumanMessage(content=input_text), HumanMessage(content=new_fr_text)]

  # supposedly, the response type should be the same of the structured output
  response = llm_struct_output.invoke(llm_input)
  # print(response.nfr_list)

  print('NFR Agent End')

  return {**state, 'NonFunctionalRequirements': response.nfr_list}