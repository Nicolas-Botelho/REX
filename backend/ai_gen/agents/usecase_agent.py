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
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Identifying the usecases and actors of the system based on the description of the system
- Identifying the events of the usecases and with actor is the performer of each event;
- Identifying the steps sequence of each event;
- Updating the given usecases with the new usecases, events and actors; and
- Returning this newly updated usecases alongside with their events and with actor is associated with each event.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Classes and Use Cases
If you do not recieve the current Use Cases, it means you are doing the first version of the Use Cases.

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the use cases, the ones you are given and the ones you created; and
- Answer in the same language the given text in writen but only use english characters;
- A usecase is considered incomplete if:
  - it has no events while events can be inferred.
- A event is considered incomplete if:
  - it has no steps while steps can be inferred; or
  - it has no actor.
- Do not return empty lists merely to satisfy the schema.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_usecases.__str__()), HumanMessage(content=current_classes.__str__())]
  # llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text)]

  response = llm_struct_output.invoke(llm_input)

  print('Usecase Agent End')

  return {**state, 'Usecases': response}