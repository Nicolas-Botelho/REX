from ai_gen.state import State
from ai_gen.llm import llm
from ai_gen.models.response_model.class_response import ClassOutput

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
- Identifying the domain classes of the system based on the description of the system and based in the given use cases
- Identifying the attributes, associoations and inheritances among the identifyied domain classes;
- Updating the given classes with the new classes, attributes, associoations and inheritances; and
- Returning this newly updated domain classes alongside with their attributes, associoations and inheritances.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Classes and Use Cases
If you do not recieve the current Classes, it means you are doing the first version of the Classes.

# About the Associations
The minimal cardinality has to be a number, but the maximal cardinality is None when the cardinality is "Many"

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the classes, the ones you are given and the ones you created; and
- Answer in the same language the given text in writen.
- A class is considered incomplete if:
  - it has no attributes while attributes can be inferred;
  - it has no associoations while associoations can be inferred.
- Before producing the final output, verify that every identified class contains all possible attributes and participates in all inferable associoations.
- Do not return empty lists merely to satisfy the schema.
'''
  
  # llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_classes.__str__()), HumanMessage(content=new_usecases.__str__())]
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text)]

  response = llm_struct_output.invoke(llm_input)

  print('Classes Agent End')

  return {**state, 'Classes': response}