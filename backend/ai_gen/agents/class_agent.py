from ai_gen.state import State, NoStructState
from ai_gen.llm import llm
from models.response_model.class_response import ClassOutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from typing import List

def call_llm(state: State):
  print('Classes Agent Start')

  input_text = state.get('InputText')
  current_classes = state.get('OldClasses')
  new_usecases = state.get('Usecases')

  llm_struct_output = llm.with_structured_output(ClassOutput)

  instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Identifying the domain Classes of the system based on the description of the system and based in the given Use Cases
- Identifying the attributes, associoations and inheritances among the identifyied domain classes;
- Updating the given Classes as needed and adding the new classes, attributes, associoations and inheritances; and
- Returning this newly updated domain classes alongside with their attributes, associoations and inheritances.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Classes
If you do not recieve the current Classes, it means you are doing the first version of the Classes.

## About the questions
All the neeeded information to create the Classes may or may not be present in the given text, in the Use Cases, or in the Classes. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the given text, in the Use Cases, or in the Classes, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# About the ClassAttribute attribute is_multiple
If is_multiple is set to true, then it means the attribute have multiple values. Otherwise, the attribute accepts only one value. E.g.:
a : list[str] # 'a' would be represented with is_multiple = true
b : str       # 'b' would be represented with is_multiple = false

# About the Associations
The minimal cardinality has to be a number, but the maximal cardinality is None when the cardinality is "Many"

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the Classes, the ones you are given and the ones you created;
- Answer in the same language the given text in writen but only use english characters;
- All Classes used in the given event's steps must be created and thry must have the exact same name as given;
- A Class is considered incomplete if:
  - it has no attributes while attributes can be inferred; or
  - it has no associoations while associoations can be inferred.
- Before producing the final output, verify that every identified class contains all possible attributes and participates in all inferable associoations; and
- Do not return empty lists merely to satisfy the schema.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_classes.__str__()), HumanMessage(content=new_usecases.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Classes Agent End')

  return {**state, 'Classes': response}

def call_llm_no_struct(state: NoStructState):
  print('Classes Agent Start')

  input_text = state.get('InputText')
  current_classes = state.get('OldClasses')
  new_usecases = state.get('Usecases')

  instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Identifying the domain Classes of the system based on the description of the system and based in the given Use Cases
- Identifying the attributes, associoations and inheritances among the identifyied domain classes;
- Updating the given Classes as needed and adding the new classes, attributes, associoations and inheritances; and
- Returning this newly updated domain classes alongside with their attributes, associoations and inheritances.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Classes
If you do not recieve the current Classes, it means you are doing the first version of the Classes.

## About the questions
All the neeeded information to create the Classes may or may not be present in the given text, in the Use Cases, or in the Classes. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the given text, in the Use Cases, or in the Classes, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# Final Instructions
- Return all the Classes, the ones you are given and the ones you created;
- Answer in the same language the given text in writen;
- All Classes used in the given event's steps must be created and thry must have the exact same name as given;
- A Class is considered incomplete if:
  - it has no attributes while attributes can be inferred; or
  - it has no associoations while associoations can be inferred.
- Before producing the final output, verify that every identified class contains all possible attributes and participates in all inferable associoations.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_classes.__str__()), HumanMessage(content=new_usecases.__str__())]

  response = llm.invoke(llm_input)

  print('Classes Agent End')

  return {**state, 'Classes': response}