import ai_gen.models.usecase as pyd
import rex.models.usecase as djg
import rex.models.klass as djg_cls

class UsecaseSaver():
  def __init__(self, class_map, attribute_map, association_map):
    self.usecase_map = {}
    self.event_map = {}
    self.actor_map = {}
    self.step_map = {}
    self.steps = []
    self.class_map = class_map
    self.attribute_map = attribute_map
    self.association_map = association_map

  def save_model(self, usecases: list[pyd.Usecase]): #, steps: list[pyd.Step]
    for uc in usecases:
      self.save_usecase(uc)

    for step in self.steps:
      self.save_step_relations(step)

  def save_usecase(self, model: pyd.Usecase):
    newUC, _ = djg.Usecase.objects.update_or_create(name=model.name, defaults={"name": model.name})

    self.usecase_map[model.name] = newUC.id

    for event in model.usecase_events:
      self.save_event(event, model.name)

  def save_event(self, model: pyd.Event, uc_name):
    if model.actor.name not in self.actor_map:
      self.save_actor(model.actor)

    newEvent, _ = djg.Event.objects.update_or_create(name=model.name, usecase_id=self.usecase_map[uc_name], defaults={"actor_id": self.actor_map[model.actor.name]})

    self.event_map[model.name] = newEvent.id

    for step in model.event_steps:
      if step.step_code not in self.step_map:
        self.save_step_class(step, newEvent.id)

  def save_actor(self, model: pyd.Actor):
    newActor, _ = djg.Actor.objects.update_or_create(name=model.name, defaults={"description":model.description})

    self.actor_map[model.name] = newActor.id

  def save_step_class(self, model: pyd.Step, event_id):
    if isinstance(model, pyd.Action):
      self.save_action_class(model, event_id)
    elif isinstance(model, pyd.Decision):
      self.save_decision_class(model, event_id)

  def save_step_relations(self, model: pyd.Step):
    if isinstance(model, pyd.Action):
      self.save_action_relations(model)
    elif isinstance(model, pyd.Decision):
      self.save_decision_relations(model)

  def save_action_class(self, model: pyd.Action, event_id):
    newStep, _ = djg.Action.objects.update_or_create(step_code=model.step_code, event_id=event_id, defaults={"category":model.category, "description":model.description, "clazz_id":self.get_or_create_class(model.class_name)})
    
    self.step_map[model.step_code] = newStep.id
    self.steps.append(model)

  def save_action_relations(self, model:pyd.Action):
    if model.next_step:
      djg.Action.objects.filter(id=self.step_map[model.step_code], step_code=model.step_code).update(next_step_id=self.step_map[model.next_step])

  def save_decision_class(self, model: pyd.Decision, event_id):
    newStep, _ = djg.Decision.objects.update_or_create(step_code=model.step_code, event_id=event_id, defaults={"description":model.description, "clazz_id":self.get_or_create_class(model.class_name)})
    
    self.step_map[model.step_code] = newStep.id
    self.steps.append(model)

  def save_decision_relations(self, model:pyd.Decision):
    if len(model.next_steps) > 0:
      djg.Decision.objects.filter(id=self.step_map[model.step_code], step_code=model.step_code).update(next_steps_id=[self.step_map[step] for step in model.next_steps])
  
  def get_or_create_class(self, class_name: str):
    if class_name not in self.class_map:
      newClass, _ = djg_cls.Class.objects.update_or_create(name=class_name, defaults={'stereotype':'kind'})
      self.class_map[class_name] = newClass.id
      return newClass.id
    return self.class_map[class_name]