from backend.ai_gen.state import State
from backend.ai_gen.llm import llm
from backend.ai_gen.response_model.requirement_response import FROutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage

def call_llm(state: State):
  print('FR Agent Start')

  input_text = state.get('InputText')

  llm_struct_output = llm.with_structured_output(FROutput)

  instruction = f'''
  # Task
  You are a Requirements Engineer tasked with extracting the functional requirements (FR) of a given text about a system.

  ## About the Requirements
  - Only extract explicit and implied requirements of the text, do not create any other requirements.
  - Use the Requirements Engineering techniques to identify the requirements of the text, even when there are more than one requirement in the same part of the text (e.g.: "The system should allow user registration by the Admin." means there is a User CRUD and some sort of Admin Login (implied, except if the text explicitly say something else about it in another moment)).
  - Explicit requirements have priority compared to implied ones. This means that if a explicit requirement contradicts a implied requirement, you should keep the explicit requirement.

  ## About the Structured Output Format for Functional Requirements (FR)
  A FR have the following parts:
  - iD: A unique integer identification of the FR;
  - priority: A integer value that defines the priority level of a requirement. It must be inside the values defined in the limits;
  - limits: A object with a min value and a max value. Defines the range of the priority that a FR can assume;
  - description: A textual description of the requirement;
  - epics: A list of epics related to that FR; and
    - iD: A unique integer identification of the epic;
    - name: The name of the epic;
    - stories: A list of the user stories of that epic; and
      - iD: A unique integer identification of that user story;
      - action: A textual description of the action of that user story;
      - goal: A textual description of the goal of that user story; and
      - performer: The performer of that user story in the format of a use case actor.
        - iD: A unique integer identification of that actor; and
        - name: The name of the actor.
    - functionalReqs: The list of the FRs related to that epic.
  - tests: A list of Gherkin test cases related to that FR.
    - given: The Given Statement in the Gherkin Test Case;
      - statement: The statement present in the Given (do not include the Given Operator. E.g.: "Given X" is writen as "X"); and
      - extension : A list of _AdditionalOperators for the Given Statement. Additional Operators can be And Statements or Or Statements.
        - statement: The statement present in the And/Or (do not include the And/Or Operator. E.g.: "And X" is writen as "X" and "Or Y" is writen as "Y").
    - when: The When Statement in the Gherkin Test Case (optional); and
      - statement: The statement present in the When (do not include the When Operator. E.g.: "When X" is writen as "X").
    - then: The Then Statement in the Gherkin Test Case.
      - statement: The statement present in the Then (do not include the Then Operator. E.g.: "Then X" is writen as "X"); and
      - extension : A list of _AdditionalOperators for the Then Statement. Additional Operators can be And Statements or Or Statements.
        - statement: The statement present in the And/Or (do not include the And/Or Operator. E.g.: "And X" is writen as "X" and "Or Y" is writen as "Y").      

  ### Abstract Classes
  Reading the Structured Output Format you may find some classes named in the following pattern '_SOME_NAME_HERE'. This (starting with underscore) means that the class is abstract, therefore if must not be instanciated in a object by its own, the instance must be of a classe that inherits it. Whenever this is the case, the classes that can be instanciated, in the place of the abstract one, are stated above.

  ## Final Instructions
  - Answer strictly in the Structured Output Format; and
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