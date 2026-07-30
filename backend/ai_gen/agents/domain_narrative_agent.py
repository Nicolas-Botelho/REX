from ai_gen.state import State, NoStructState
from ai_gen.llm import llm
from models.response_model.narrative_response import NarrativeOutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from typing import List

def call_llm(state: State):
  print('Narrative Agent Start')

  input_text = state.get('InputText')
  current_narrative = state.get('OldDomainNarrative')

  llm_struct_output = llm.with_structured_output(NarrativeOutput)

  instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Identifying the context of the system;
- Identifying the users of the system;
- Identifying the functionalities of the system;
- Updating the current Domain Narrative, if there is one, with the new information about the system; and
- Returning this new Domain Narrative with the description of the domain (context), the users and the functionalities of the system.

# About the Input
You are going to recieve the following input:
- The text you must read; and
- The current version of the Domain Narrative.

## About the current Domain Narrative
If you do not recieve the current Domain Narrative, it means you are doing the first version of the Domain Narrative.

## About the questions
All the neeeded information to create the Domain Narrative may or may not be present in the current Domain Narrative, and in the given text. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the current Domain Narrative, or in the given text, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return new domain narrative;
- Answer in the same language the given text is writen; and
- Do not return empty lists merely to satisfy the schema.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_narrative.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Narrative Agent End')

  return {**state, 'DomainNarrative': response}

def call_llm_no_struct(state: NoStructState):
  print('Narrative Agent Start')

  input_text = state.get('InputText')
  current_narrative = state.get('OldDomainNarrative')

  instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Identifying the context of the system;
- Identifying the users of the system;
- Identifying the functionalities of the system;
- Updating the current Domain Narrative, if there is one, with the new information about the system; and
- Returning this new Domain Narrative with the description of the domain (context), the users and the functionalities of the system.

# About the Input
You are going to recieve the following input:
- The text you must read; and
- The current version of the Domain Narrative.

## About the current Domain Narrative
If you do not recieve the current Domain Narrative, it means you are doing the first version of the Domain Narrative.

## About the questions
All the neeeded information to create the Domain Narrative may or may not be present in the current Domain Narrative, and in the given text. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the current Domain Narrative, or in the given text, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# Final Instructions
- Return new domain narrative;
- Answer in the same language the given text is writen.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_narrative.__str__())]

  response = llm.invoke(llm_input)

  print('Narrative Agent End')

  return {**state, 'DomainNarrative': response.content}