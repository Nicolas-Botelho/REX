import ai_gen.models.usecase as pyd
import rex.models.usecase as djg

class UsecaseSaver():
  def __init__(self, class_map, attribute_map, relation_map):
    self.usecase_map = {}
    self.event_map = {}
    self.actor_map = {}
    self.step_map = {}
    self.class_map = class_map
    self.attribute_map = attribute_map
    self.relation_map = relation_map

  def maps(self):
    return

  def save_model(self, usecases: list[pyd.Usecase], steps: list[pyd.Step]):
    for uc in usecases:
      self.save_usecase(uc)
    
    steps.reverse()

    for step in steps:
      self.save_step_class(step)
    for step in steps:
      self.save_step_relations(step)

    return self.maps()

  def save_usecase(self, model: pyd.Usecase):
    newUC, _ = djg.Usecase.objects.update_or_create(name=model.name, defaults={"name": model.name})

    self.usecase_map[model.id] = newUC.id

    for event in model.usecase_events:
      self.save_event(event, model.id)

  def save_event(self, model: pyd.Event, uc_id):
    if model.actor.id not in self.actor_map:
      self.save_actor(model.actor)

    if model.first_step.id not in self.step_map:
      self.save_step_class(model.first_step)

    newEvent, _ = djg.Event.objects.update_or_create(name=model.name, usecase_id=self.usecase_map[uc_id], defaults={"actor_id": self.actor_map[model.actor.id], "first_step_id": self.step_map[model.first_step.id]})

    self.event_map[model.id] = newEvent.id

  def save_actor(self, model: pyd.Actor):
    newActor, _ = djg.Actor.objects.update_or_create(name=model.name, defaults={"description":model.description})

    self.actor_map[model.id] = newActor.id

  def save_step_class(self, model: pyd.Step):
    if isinstance(model, pyd.Action):
      self.save_action_class(model)
    elif isinstance(model, pyd.Decision):
      self.save_decision_class(model)

  def save_step_relations(self, model: pyd.Step):
    if isinstance(model, pyd.Action):
      self.save_action_relations(model)
    elif isinstance(model, pyd.Decision):
      self.save_decision_relations(model)

  def save_action_class(self, model: pyd.Action):
    if isinstance(model, pyd.ModifyAction):
      newModifyAction, _ = djg.ModifyAction.objects.update_or_create(
        description=model.description,
        related_classes_id=[self.class_map[cls.id] for cls in model.related_classes],
        next_step_id=None)
      self.step_map[model.id] = newModifyAction.id

    elif isinstance(model, pyd.TextReadAction):
      newReadAction, _ = djg.TextReadAction.objects.update_or_create(
        description=model.description,
        match_percent=model.match_percent,
        related_classes_id=[self.class_map[cls.id] for cls in model.related_classes],
        read_attributes=[self.attribute_map[attr.id] for attr in model.read_attributes],
        next_step_id=None)
      self.step_map[model.id] = newReadAction.id

    elif isinstance(model, pyd.ReadAction):
      newReadAction, _ = djg.ReadAction.objects.update_or_create(
        description=model.description,
        related_classes_id=[self.class_map[cls.id] for cls in model.related_classes],
        read_attributes_id=[self.attribute_map[attr.id] for attr in model.read_attributes],
        next_step_id=None)
      self.step_map[model.id] = newReadAction.id

    else:
      newAction, _ = djg.Action.objects.update_or_create(
        description=model.description,
        next_step_id=None)
      self.step_map[model.id] = newAction.id

  def save_decision_class(self, model: pyd.Decision):
    newDecision, _ = djg.Decision.objects.update_or_create(description=model.description, 
    next_steps_id=None)
    self.step_map[model.id] = newDecision.id

  def save_action_relations(self, model: pyd.Action):
    if model.next_step:
      action = djg.Action.objects.get(pk=self.step_map[model.id])
      action.next_step_id = model.next_step
      action.save()

  def save_decision_relations(self, model: pyd.Decision):
    decision = djg.Decision.objects.get(pk=self.step_map[model.id])
    decision.next_steps.set([self.step_map[step] for step in model.next_steps])
    decision.save()