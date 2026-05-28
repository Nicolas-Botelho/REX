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
You are a Requirements Engineer tasked with reading a text about a system and defining its Domain Classes and their attributes, relations and inheritances.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases
- The current version of the Event's Steps; and
- The current version of the Classes.

## About the current Classes and Use Cases
If you do not recieve the current Classes, it means you are doing the first version of the Classes.

# About the Classes
{open("ai_gen/models/docs/classes.md", "r").read()}

# About the Use Cases and Event's Steps
{open("ai_gen/models/docs/usecases.md", "r").read()}

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the classes, the ones you are given and the ones you created; and
- Answer in the same language the given text in writen.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_classes.__str__()), HumanMessage(content=new_usecases.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Classes Agent End')

  return {**state, 'Classes': response}