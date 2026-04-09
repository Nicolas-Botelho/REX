import streamlit as st
import requests

def load_class():
  return load("classes", "class")

def load_enum():
  return load("classes", "enum")

def load_usecases():
  return load("use_cases", "usecase")

def load_usecase_actor():
  return load("use_cases", "actor")

def load(module: str, cls: str):
  try:
    BACKEND_URL = st.get_option("server.corsAllowedOrigins")[0]

    response = requests.get(url=f"{BACKEND_URL}/{module}/{cls}/")  

    return response.json()
  except Exception as e:
    return [{"error" : e.__dict__}]

# [
#   {
#     "id": 1,
#     "class_primitive_attrs": [
#       {
#         "id": 1,
#         "name": "name",
#         "attr_type": "string",
#         "klass": 1
#       }
#     ],
#     "class_enum_attrs": [],
#     "class_relations": [
#       {
#         "id": 1,
#         "rcr_as_srcs": [
#           {
#             "id": 1,
#             "src": 1,
#             "tgt": 2
#           }
#         ],
#         "rcr_as_tgts": [],
#         "minim": 1,
#         "maxim": 1,
#         "ref_class": 1
#       }
#     ],
#     "name": "User"
#   },
#   {
#     "id": 2,
#     "class_primitive_attrs": [
#       {
#         "id": 2,
#         "name": "name",
#         "attr_type": "string",
#         "klass": 2
#       },
#       {
#         "id": 3,
#         "name": "numberedPriorityMinRange",
#         "attr_type": "integer",
#         "klass": 2
#       },
#       {
#         "id": 4,
#         "name": "numberedPriorityMaxRange",
#         "attr_type": "integer",
#         "klass": 2
#       }
#     ],
#     "class_enum_attrs": [
#       {
#         "id": 1,
#         "enum": {
#           "id": 1,
#           "enum_values": [
#             {
#               "id": 1,
#               "value": "BINARY",
#               "enum": 1
#             },
#             {
#               "id": 2,
#               "value": "NUMBERED",
#               "enum": 1
#             },
#             {
#               "id": 3,
#               "value": "NOT_PRESENT",
#               "enum": 1
#             }
#           ],
#           "name": "PriorityMethodType"
#         },
#         "name": "priorityMethodType",
#         "klass": 2
#       },
#       {
#         "id": 2,
#         "enum": {
#           "id": 2,
#           "enum_values": [
#             {
#               "id": 4,
#               "value": "ZERO_IS_MAX",
#               "enum": 2
#             },
#             {
#               "id": 5,
#               "value": "ZERO_IS_MIN",
#               "enum": 2
#             }
#           ],
#           "name": "NumberedPriorityOrder"
#         },
#         "name": "numberedPriorityOrder",
#         "klass": 2
#       }
#     ],
#     "class_relations": [
#       {
#         "id": 2,
#         "rcr_as_srcs": [],
#         "rcr_as_tgts": [
#           {
#             "id": 1,
#             "src": 1,
#             "tgt": 2
#           }
#         ],
#         "minim": 0,
#         "maxim": null,
#         "ref_class": 2
#       },
#       {
#         "id": 3,
#         "rcr_as_srcs": [
#           {
#             "id": 2,
#             "src": 3,
#             "tgt": 4
#           }
#         ],
#         "rcr_as_tgts": [],
#         "minim": 1,
#         "maxim": 1,
#         "ref_class": 2
#       }
#     ],
#     "name": "List"
#   },
#   {
#     "id": 3,
#     "class_primitive_attrs": [
#       {
#         "id": 5,
#         "name": "description",
#         "attr_type": "string",
#         "klass": 3
#       },
#       {
#         "id": 6,
#         "name": "binaryPriority",
#         "attr_type": "boolean",
#         "klass": 3
#       },
#       {
#         "id": 7,
#         "name": "numberedPriority",
#         "attr_type": "integer",
#         "klass": 3
#       }
#     ],
#     "class_enum_attrs": [],
#     "class_relations": [
#       {
#         "id": 4,
#         "rcr_as_srcs": [],
#         "rcr_as_tgts": [
#           {
#             "id": 2,
#             "src": 3,
#             "tgt": 4
#           }
#         ],
#         "minim": 0,
#         "maxim": null,
#         "ref_class": 3
#       }
#     ],
#     "name": "Task"
#   }
# ]

# [
#   {
#     "id": 1,
#     "usecase_events": [
#       {
#         "id": 1,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 1,
#             "system": false,
#             "description": "User initiates the creation of a new list.",
#             "event": 1
#           },
#           {
#             "id": 2,
#             "system": true,
#             "description": "System prompts the user for list name.",
#             "event": 1
#           },
#           {
#             "id": 3,
#             "system": false,
#             "description": "User provides the list name.",
#             "event": 1
#           },
#           {
#             "id": 4,
#             "system": true,
#             "description": "System prompts the user to define the priority method for the list (binary, numbered, or not present).",
#             "event": 1
#           },
#           {
#             "id": 5,
#             "system": false,
#             "description": "User selects a priority method.",
#             "event": 1
#           },
#           {
#             "id": 6,
#             "system": true,
#             "description": "If 'numbered' priority is selected, System prompts the user to define the range and order (0 is max or min priority).",
#             "event": 1
#           },
#           {
#             "id": 7,
#             "system": false,
#             "description": "If 'numbered' priority is selected, User defines the range and order.",
#             "event": 1
#           },
#           {
#             "id": 8,
#             "system": false,
#             "description": "User confirms the list creation.",
#             "event": 1
#           },
#           {
#             "id": 9,
#             "system": true,
#             "description": "System creates the new list with the specified name and priority method.",
#             "event": 1
#           }
#         ],
#         "name": "Create List",
#         "usecase": 1
#       },
#       {
#         "id": 4,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 25,
#             "system": false,
#             "description": "User initiates viewing available lists.",
#             "event": 4
#           },
#           {
#             "id": 26,
#             "system": true,
#             "description": "System retrieves and displays all lists, including their names and defined priority methods.",
#             "event": 4
#           }
#         ],
#         "name": "View Lists",
#         "usecase": 1
#       },
#       {
#         "id": 5,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 27,
#             "system": false,
#             "description": "User selects a list from the displayed lists to delete.",
#             "event": 5
#           },
#           {
#             "id": 28,
#             "system": true,
#             "description": "System prompts the user for confirmation to delete the selected list and all its tasks.",
#             "event": 5
#           },
#           {
#             "id": 29,
#             "system": false,
#             "description": "User confirms the deletion.",
#             "event": 5
#           },
#           {
#             "id": 30,
#             "system": true,
#             "description": "System deletes the selected list and all its associated tasks.",
#             "event": 5
#           }
#         ],
#         "name": "Delete List",
#         "usecase": 1
#       },
#       {
#         "id": 6,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 31,
#             "system": false,
#             "description": "User selects a list to modify.",
#             "event": 6
#           },
#           {
#             "id": 32,
#             "system": false,
#             "description": "User initiates the update of list details (name or priority method).",
#             "event": 6
#           },
#           {
#             "id": 33,
#             "system": true,
#             "description": "System displays current list name and priority method and prompts for changes.",
#             "event": 6
#           },
#           {
#             "id": 34,
#             "system": false,
#             "description": "User provides a new list name or selects a new priority method.",
#             "event": 6
#           },
#           {
#             "id": 35,
#             "system": true,
#             "description": "If 'numbered' priority is selected, System prompts the user to define the range and order (0 is max or min priority).",
#             "event": 6
#           },
#           {
#             "id": 36,
#             "system": false,
#             "description": "If 'numbered' priority is selected, User defines the range and order.",
#             "event": 6
#           },
#           {
#             "id": 37,
#             "system": false,
#             "description": "User confirms the updates.",
#             "event": 6
#           },
#           {
#             "id": 38,
#             "system": true,
#             "description": "System updates the list with the new name and/or priority method.",
#             "event": 6
#           }
#         ],
#         "name": "Update List Details",
#         "usecase": 1
#       }
#     ],
#     "name": "Manage Lists"
#   },
#   {
#     "id": 2,
#     "usecase_events": [
#       {
#         "id": 2,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 10,
#             "system": false,
#             "description": "User selects an existing list.",
#             "event": 2
#           },
#           {
#             "id": 11,
#             "system": false,
#             "description": "User initiates adding a new task to the selected list.",
#             "event": 2
#           },
#           {
#             "id": 12,
#             "system": true,
#             "description": "System prompts the user for task description.",
#             "event": 2
#           },
#           {
#             "id": 13,
#             "system": false,
#             "description": "User provides the task description.",
#             "event": 2
#           },
#           {
#             "id": 14,
#             "system": true,
#             "description": "If the selected list has a priority method, System prompts the user to set the task's priority according to the list's method.",
#             "event": 2
#           },
#           {
#             "id": 15,
#             "system": false,
#             "description": "If applicable, User sets the task's priority.",
#             "event": 2
#           },
#           {
#             "id": 16,
#             "system": false,
#             "description": "User confirms the task creation.",
#             "event": 2
#           },
#           {
#             "id": 17,
#             "system": true,
#             "description": "System adds the new task to the selected list with the specified description and priority (if applicable).",
#             "event": 2
#           }
#         ],
#         "name": "Add Task to List",
#         "usecase": 2
#       },
#       {
#         "id": 3,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 18,
#             "system": false,
#             "description": "User selects a list that has a priority method.",
#             "event": 3
#           },
#           {
#             "id": 19,
#             "system": false,
#             "description": "User selects a task within the chosen list.",
#             "event": 3
#           },
#           {
#             "id": 20,
#             "system": false,
#             "description": "User initiates changing the selected task's priority.",
#             "event": 3
#           },
#           {
#             "id": 21,
#             "system": true,
#             "description": "System displays the current priority and prompts for a new priority based on the list's defined method.",
#             "event": 3
#           },
#           {
#             "id": 22,
#             "system": false,
#             "description": "User sets the new priority for the task.",
#             "event": 3
#           },
#           {
#             "id": 23,
#             "system": false,
#             "description": "User confirms the priority change.",
#             "event": 3
#           },
#           {
#             "id": 24,
#             "system": true,
#             "description": "System updates the task's priority in the list.",
#             "event": 3
#           }
#         ],
#         "name": "Update Task Priority",
#         "usecase": 2
#       },
#       {
#         "id": 7,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 39,
#             "system": false,
#             "description": "User selects an existing list.",
#             "event": 7
#           },
#           {
#             "id": 40,
#             "system": false,
#             "description": "User initiates viewing tasks within the selected list.",
#             "event": 7
#           },
#           {
#             "id": 41,
#             "system": true,
#             "description": "System retrieves and displays all tasks in the selected list, including their descriptions and priorities (if applicable).",
#             "event": 7
#           }
#         ],
#         "name": "View Tasks in List",
#         "usecase": 2
#       },
#       {
#         "id": 8,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 42,
#             "system": false,
#             "description": "User selects an existing list.",
#             "event": 8
#           },
#           {
#             "id": 43,
#             "system": false,
#             "description": "User selects a task from the displayed tasks to delete.",
#             "event": 8
#           },
#           {
#             "id": 44,
#             "system": true,
#             "description": "System prompts the user for confirmation to delete the selected task.",
#             "event": 8
#           },
#           {
#             "id": 45,
#             "system": false,
#             "description": "User confirms the deletion.",
#             "event": 8
#           },
#           {
#             "id": 46,
#             "system": true,
#             "description": "System deletes the selected task from the list.",
#             "event": 8
#           }
#         ],
#         "name": "Delete Task",
#         "usecase": 2
#       },
#       {
#         "id": 9,
#         "actor": {
#           "id": 1,
#           "name": "User",
#           "description": "The user of the ToDo List application."
#         },
#         "event_steps": [
#           {
#             "id": 47,
#             "system": false,
#             "description": "User selects an existing list.",
#             "event": 9
#           },
#           {
#             "id": 48,
#             "system": false,
#             "description": "User selects a task within the chosen list.",
#             "event": 9
#           },
#           {
#             "id": 49,
#             "system": false,
#             "description": "User initiates updating task details (e.g., description, completion status).",
#             "event": 9
#           },
#           {
#             "id": 50,
#             "system": true,
#             "description": "System displays current task details (description, completion status) and prompts for changes.",
#             "event": 9
#           },
#           {
#             "id": 51,
#             "system": false,
#             "description": "User provides a new description or toggles the task's completion status.",
#             "event": 9
#           },
#           {
#             "id": 52,
#             "system": false,
#             "description": "User confirms the updates.",
#             "event": 9
#           },
#           {
#             "id": 53,
#             "system": true,
#             "description": "System updates the task with the new description and/or completion status.",
#             "event": 9
#           }
#         ],
#         "name": "Update Task Details",
#         "usecase": 2
#       }
#     ],
#     "name": "Manage Tasks"
#   }
# ]