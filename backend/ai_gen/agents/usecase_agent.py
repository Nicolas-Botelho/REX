from ai_gen.state import State, NoStructState
from ai_gen.llm import llm
from models.response_model.usecase_response import UsecaseOutput

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from typing import List

instruction = f'''
# Task
You are a Requirements Engineer tasked with:
- Reading a text description of a system;
- Identifying the Use Cases and Actors of the system based on the description of the system
- Identifying the Events of the Use Cases and which Actor is the performer of each Event;
- Identifying the Steps sequence of each event;
- Updating the given Use Cases as needed and adding the new Use Cases, events and actors; and
- Returning this newly updated Use Cases alongside with their events and with actor is associated with each event.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Domain Narrative;
- The current version of the Requirements;
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Use Cases
If you do not recieve the current Use Cases, it means you are doing the first version of the Use Cases.

## About the Steps
- The Step codes must be labeled strictly following the structure below:
  - S000. E.g.: S001, S002, S003, etc.
- Each step can be associated with 0 or 1 class. If it is needed to associate a step with multiple classes, it must be separated in multiple steps, one for each class.

## Actions Operations
- Data Operations: Operations relevant to the system's data and informations. When informing the attributes, list them individually by name and associating to their respective class, even if all of the class' attributes will be used;
- Complex Operations: Other relevant operations that do not fit the categories inside data operation (e.g.: API Calls);
- Nav Operations: Operations of executing another events inside the current event. It's categories reflect how these events will appear in the interface (e.g.: as a modal or navigating to the new screen); and
- None: Used for actions that are not relevent for the system's data/informations directly (e.g.: user input and how a output is presented).

## About the questions
All the neeeded information to create the Use Cases may or may not be present in the given text, in the Domain Narrative, in the Requirements, in the Use Cases, or in the Classes. If any information is needed but is not present, add a question about it. Also, if a question ask about a information what is already present in the given text, in the Domain Narrative, in the Requirements, in the Use Cases, or in the Classes, consider that quesiton answered and remove the question. Finally, try to answer as many question as possible with the given informations.

# Final Instructions
- Answer strictly in the Structured Output Format;
- Return all the Use Cases, the ones you are given and the ones you created;
- The Classes in the Events Steps are Domain Classes
- Answer in the same language the given text in writen but only use english characters;
- A Use Case is considered incomplete if:
  - it has no events while events can be inferred.
- A event is considered incomplete if:
  - it has no steps while steps can be inferred; or
  - it has no actor.
- Do not return empty lists merely to satisfy the schema.
'''

def call_llm(state: State):
  print('Usecase Agent Start')

  input_text = state.get('InputText')
  current_classes = state.get('OldClasses')
  current_usecases = state.get('OldUsecases')
  new_narrative = state.get('DomainNarrative')
  new_requirements = state.get('Requirements')

  llm_struct_output = llm.with_structured_output(UsecaseOutput)
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=new_narrative.__str__()), HumanMessage(content=new_requirements.__str__()), HumanMessage(content=current_usecases.__str__()), HumanMessage(content=current_classes.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Usecase Agent End')

  return {**state, 'Usecases': response}

def call_llm_no_struct(state: NoStructState):
  print('Usecase Agent Start')

  input_text = state.get('InputText')
  current_classes = state.get('OldClasses')
  current_usecases = state.get('OldUsecases')
  new_narrative = state.get('DomainNarrative')
  new_requirements = state.get('Requirements')
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=new_narrative.__str__()), HumanMessage(content=new_requirements.__str__()), HumanMessage(content=current_usecases.__str__()), HumanMessage(content=current_classes.__str__())]

  response = llm.invoke(llm_input)

  print('Usecase Agent End')

  return {**state, 'Usecases': response.content}