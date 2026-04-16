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
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Classes and Use Cases
If you do not recieve the current Use Cases, it means you are doing the first version of the Use Cases.

If you do recieve them you should consider that they are 100% correct and should never contradict them. Also, do not add anything to them, only create new Use Cases.

# About the Use Cases
The Use Cases are have the following division:
- Use Case: Define a group of related functionalities of the system;
- Event: One functionality of the system; Must be associated with a use case;
- Actor: The actor that can execute a event; Must be associated with a event; and
- Step: A step of a event; Must be associated with a event.

## About the Structured Output Format
The Structured Output have the following fields:
- usecases: All the created usecases;
- events: All the created events;
- actors: All the created actors; and
- steps: All the created steps.

### Usecase Fields
- semantic_id: string; must be unique among the usecases; must be snake_case; use case identification; and
- name: string; must be unique; use case name.

### Event Fields
- semantic_id: string; must be unique among the events; must be snake_case; event identification;
- name: string; must be unique in the usecase it is part of; event name;
- actor: positive integer; must be a existent actor semantic_id; actor that executes the event; and
- usecase: positive integer; must be a existent usecase semantic_id; usecase that the event is part of.

### Actor Fields
- semantic_id: string; must be unique among the actors; must be snake_case; actor identification;
- name: string; must be unique; actor name; and
- description: string or None; optional; optional description of the actor.

### Step Fields
- semantic_id: string; must be unique among the steps; must be snake_case; step identification;
- system: boolean; True or False; False = Actor executed step and True = System executed step;
- description: string; no restrictions; description of the executed actions in the step; and
- event: int; must be a existent event semantic_id; event that the step is part of.

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return only the newly created use cases, do not return the use cases you recieved; and
- Answer in the same language the given text in writen.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_usecases.__str__()), HumanMessage(content=current_classes.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Usecase Agent End')

  return {**state, 'Usecases': response}