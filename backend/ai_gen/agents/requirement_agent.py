from ai_gen.state import State, NoStructState
from ai_gen.llm import llm
from models.response_model.requirement_response import RequirementOutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from typing import List

def call_llm(state: State):
  print('Requirement Agent Start')

  input_text = state.get('InputText')
  current_requirements = state.get('OldRequirements')
  new_narrative = state.get('DomainNarrative')

  llm_struct_output = llm.with_structured_output(RequirementOutput)

  instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Reading the Domain Narrative of the system;
- Identifying the Requirements of the system;
- Categorize each Requirement as:
  - Functional Requirement: Describe a funcionality of the system;
  - Non Functional Requirement: Describe a limitation or a quality constraint (e.g.: performance, security, usability, reliability, etc) of the system; or
  - Business Rule: Describe a domain constraint or policy that the system must respect (e.g.: internal regulaments, laws, company/market standards).
- Identifying the dependencies of the Requirements, ensuring that there is no circular dependencies;
- Updating the current Requirements as needed and adding the new ones; and
- Returning this newly updated Requirements with their categories and dependencies.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Domain Narrative; and
- The current version of the Requirements.

## About the current Requirements
If you do not recieve the current Requirements, it means you are doing the first version of the Requirements.

## About the questions
All the neeeded information to create the Requirements may or may not be present in the given text, in the Domain Narrative, or in the Requirements. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the given text, in the Domain Narrative, or in the Requirements, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the Requirements, the ones you are given and the ones you created;
- Answer in the same language the given text in writen but only use english characters; and
- Do not return empty lists merely to satisfy the schema.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=new_narrative.__str__()), HumanMessage(content=current_requirements.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Requirement Agent End')

  return {**state, 'Requirements': response}

def call_llm_no_struct(state: NoStructState):
  print('Requirement Agent Start')

  input_text = state.get('InputText')
  current_requirements = state.get('OldRequirements')
  new_narrative = state.get('DomainNarrative')

  instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Reading the Domain Narrative of the system;
- Identifying the Requirements of the system;
- Categorize each Requirement as:
  - Functional Requirement: Describe a funcionality of the system;
  - Non Functional Requirement: Describe a limitation or a quality constraint (e.g.: performance, security, usability, reliability, etc) of the system; or
  - Business Rule: Describe a domain constraint or policy that the system must respect (e.g.: internal regulaments, laws, company/market standards).
- Identifying the dependencies of the Requirements, ensuring that there is no circular dependencies;
- Updating the current Requirements as needed and adding the new ones; and
- Returning this newly updated Requirements with their categories and dependencies.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Domain Narrative; and
- The current version of the Requirements.

## About the current Requirements
If you do not recieve the current Requirements, it means you are doing the first version of the Requirements.

## About the questions
All the neeeded information to create the Requirements may or may not be present in the given text, in the Domain Narrative, or in the Requirements. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the given text, in the Domain Narrative, or in the Requirements, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# Final Instructions
- Return all the Requirements, the ones you are given and the ones you created; and
- Answer in the same language the given text in writen.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=new_narrative.__str__()), HumanMessage(content=current_requirements.__str__())]

  response = llm.invoke(llm_input)

  print('Requirement Agent End')

  return {**state, 'Requirements': response.content}