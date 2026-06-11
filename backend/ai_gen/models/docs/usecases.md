# Usecases Model Definition

## Usecase
An usecase.

- id (int): integer usecase id;
- name (str): unique name of the usecase; and
- usecase_events (list[Event]): events of the usecase.

## Event
An event: ordered sequence of steps executed by an actor that especify one or more functionalities required at the system.

- id (int): integer event id;
- name (str): name of the event;
- actor (Actor): actor that executes the event; and
- first_step (Action | Decision | Modify Action | Read Action | Text Read Action): the first step of the event.

## Actor
An actor: executor of events.

- id (int): integer actor id;
- name (str): unique name of the actor; and
- description (str): description of the actor.

## Step
Definition of a step: action or decision made that contributes to the goal of the event it is part of.

### Action
An action: step for when a generic action is made.

- id (int): integer step id;
- description (str): description of the action; and
- next_step (int | None): step id of the next step. If it is None, this is a final step.

### Modify Action
A modify action: specific action for when an action modifies one or more domain classes.

- id (int): integer step id;
- description (str): description of the action;
- next_step (int | None): step id of the next step. If it is None, this is a final step;
- action_type (str): type of modification made to the class/classes. Has to be from one of the followinf types: create, update or delete; and
- related_classes (list[Class]): classes modified by the action.

### Read Action
A read action: specific action for when an action read one or more attributes from domain classes.

- id (int): integer step id;
- description (str): description of the action;
- next_step (int | None): step id of the next step. If it is None, this is a final step;
- related_classes (list[Class]): classes read by the action; and
- read_attributes (list[Attribute]): read attributes of the related classes.

### Text Read Action
A text read action: specific read action for when a read action is only for string attributes and uses a smart filter (with a match percent).

- id (int): integer step id;
- description (str): description of the action;
- match_percent (float): percentual of a match to return the value in a filter;
- next_step (int | None): step id of the next step. If it is None, this is a final step;
- related_classes (list[Class]): classes read by the action; and
- read_attributes (list[Attribute]): read attributes of the related classes.

### Decision
A decision: step for when a decision is made and it can lead to one of multiple next steps depending of it's results. Do not implies any action other than the decision.

- id (int): integer step id;
- description (str): description of the decision. it includes the description of the conditions to go to each next step; and
- next_steps (list[int]): step ids of the next steps.