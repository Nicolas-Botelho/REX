from ai_gen.state import State
from ai_gen.llm import llm
from ai_gen.models.response_model.usecase_response import UsecaseOutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from typing import List

def call_llm(state: State):
  print('Usecase Agent Start')

  input_text = state.get('InputText')
  current_classes = state.get('OldClasses')
  current_usecases = state.get('OldUsecases')

  llm_struct_output = llm.with_structured_output(UsecaseOutput)

  instruction = f'''
# Task
You are a Requirements Engineer tasked with reading a text about a system and defining its Funtional Requirements in the form of Use Cases.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases;
- The current version of the Event's Steps; and
- The current version of the Classes.

## About the current Classes and Use Cases
If you do not recieve the current Use Cases, it means you are doing the first version of the Use Cases.

# About the Classes
{open("ai_gen/models/docs/classes.md", "r").read()}

# About the Use Cases and Event's Steps
{open("ai_gen/models/docs/usecases.md", "r").read()}

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the use cases, the ones you are given and the ones you created; and
- Answer in the same language the given text in writen.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_usecases.__str__()), HumanMessage(content=current_classes.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Usecase Agent End')

  return {**state, 'Usecases': response}