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
You are a Requirements Engineer tasked with reading a text about a system and defining its Domain Classes.

# About the Input
You are going to recieve the following input:
- The text you must read;
- The current version of the Use Cases; and
- The current version of the Classes.

## About the current Classes and Use Cases
If you do not recieve the current Classes, it means you are doing the first version of the Classes.

If you do recieve them you should consider that they are 100% correct and should never contradict them. Also, do not add anything to them, only create new Use Cases.

# About the Classes
The Classes are have the following division:
- Class: Define a class in the system;
- ClassAttributePrim: Define a class attribute that is one of the primitive types (integer, string, boolean and float);
- ClassAttributeEnum: Define a class attribute that is a enum;
- Enum: Define a enum in the system
- EnumAttribute: Define a attribute/value from a enum;
- RelationClassReference: Define one side of a relation between 2 classes; and
- Relation: Define a relation between 2 classes (using one RelationClassReference for each).

## About the Structured Output Format
The Structured Output have the following fields:
- classes: All the created classes;
- class_primitive_attributes: All the created class attributes from the primitive type;
- class_enum_attributes: All the created class attributes that are enums;
- enums: All the created enums;
- enum_attributes: All the created enum attributes;
- relation_class_references: All the created references between a class and a relation; and
- relations: All the created relations.

### Class Fields
- iD: positive integer; must be unique; class identification; and
- name: string; must be unique; class name.

### Class Primitive Attribute Fields
- iD: positive integer; must be unique; class primitive attribute identification;
- name: string; must be unique in the attributes of the class it is part of; class primitive attribute name;
- attr_type: string; must be one of the primitive types (integer, string, boolean or float); type of the attribute; and
- klass: integer; must be a existent class iD; class that the attribute is part of.

### Class Enum Attribute Fields
- iD: positive integer; must be unique; class enum attribute identification;
- name: string; must be unique in the attributes of the class it is part of; class enum attribute name;
- enum: integer; must be a existent enum iD; enum used to define the attribute; and
- klass: integer; must be a existent class iD; class that the attribute is part of.

### Enum Fields
- iD: positive integer; must be unique; enum identification; and
- name: string; must be unique; enum name.

### Enum Attribute Fields
- iD: positive integer; must be unique; enum attribute identification;
- name: string; must be unique in the enum it is part of; enum attribute name; and
- enum: integer; must be a existent enum iD; enum that the attribute is part of.

### Relation Class Reference Fields
- iD: positive integer; must be unique; relation class reference identification;
- minim: integer; must be lower than or equal to maxim; minimum of that class in the relation;
- maxim: integer or None; must be higher than or equal to minim and not zero; maximum of that class in the relation or None to mean "N"; and
- ref_class: integer; must be a existent class iD; referenciated class.

### Relation Fields
- iD: positive integer; must be unique; relation identification;
- src: integer; must be a existent relation class reference iD; source of the relation;
- tgt: integer; must be a existent relation class reference iD; target of the relation;

# Final Instructions
- Answer strictly in the Structured Output Format; and
- Answer in the same language the given text in writen.
'''
  
  llm_input = [SystemMessage(content=instruction), HumanMessage(content=input_text), HumanMessage(content=current_classes.__str__()), HumanMessage(content=new_usecases.__str__())]

  response = llm_struct_output.invoke(llm_input)

  print('Classes Agent End')

  return {**state, 'Classes': response}