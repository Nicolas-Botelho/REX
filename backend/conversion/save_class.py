import ai_gen.models.klass as pyd
import rex.models.klass as djg

class ClassSaver():
  def __init__(self):
    self.class_map = {}
    self.enum_map = {}
    self.attribute_map = {}
    self.relation_map = {}

  def maps(self):
    return {"class_map": self.class_map, "enum_map": self.enum_map, "attribute_map": self.attribute_map, "relation_map": self.relation_map}

  def save_model(self, models: list[pyd.Class]):
    for model in models:
      self.save_class_model(model)
    for model in models:
      self.save_class_relations(model)

    return self.maps()

  def save_class_model(self, model: pyd.Class):
    newClass, _ = djg.Class.objects.update_or_create(name=model.name, defaults={"stereotype": model.stereotype})

    self.class_map[model.id] = newClass.id

    for attr in model.class_attrs:
      if isinstance(attr, pyd.ClassAttributeEnum):
        self.save_enumattr(attr)
      elif isinstance(attr, pyd.ClassAttributePrim):
        self.save_primattr(attr)
  
  def save_class_relations(self, model: pyd.Class):
    for rel in model.class_relations:
      self.save_relation(rel)

    for child_rel in model.class_childs:
      self.save_inherit(child_rel)
    
    for par_rel in model.class_parents:
      self.save_inherit(par_rel)
  
  def save_enumattr(self, model: pyd.ClassAttributeEnum):
    if model.enum.id not in self.enum_map:
      newEnum, _ = djg.Enum.objects.update_or_create(name=model.enum.name, defaults={"name": model.enum.name})
      self.enum_map[model.enum.id] = newEnum.id

      for value in model.enum.enum_values:
        djg.EnumAttribute.objects.update_or_create(value=value.value, enum_id=self.enum_map[value.enum.id])

    newAttr, _ = djg.ClassAttributeEnum.objects.update_or_create(name=model.name, klass_id=self.class_map[model.klass], defaults={"enum_id": self.enum_map[model.enum.id]})

    self.attribute_map[model.id] = newAttr.id

  def save_primattr(self, model: pyd.ClassAttributePrim):
    newAttr, _ = djg.ClassAttributePrim.objects.update_or_create(name=model.name, klass_id=self.class_map[model.klass], defaults={"attr_type":model.attr_type})

    self.attribute_map[model.id] = newAttr.id

  def save_relation(self, model: pyd.RelationClassReference):
    """
    Saves a relation given both classes are already saved in the current run
    """

    firstRCR, _ = djg.RelationClassReference.objects.update_or_create(minim=model.minim, maxim=model.maxim, ref_class_id=self.class_map[model.ref_class.id])

    if model.rcr_as_src:
      secondRCR, _ = djg.RelationClassReference.objects.update_or_create(minim=model.rcr_as_src.tgt.minim, maxim=model.rcr_as_src.tgt.maxim, ref_class_id=self.class_map[model.rcr_as_src.tgt.ref_class.id])

      newRel, _ = djg.Relation.objects.update_or_create(src_id=firstRCR.id, tgt_id=secondRCR.id)

      self.relation_map[model.id] = newRel.id
    
    elif model.rcr_as_tgt:
      secondRCR = djg.RelationClassReference.objects.update_or_create(minim=model.rcr_as_tgt.src.minim, maxim=model.rcr_as_tgt.src.maxim, ref_class_id=self.class_map[model.rcr_as_tgt.src.ref_class.id])

      newRel, _ = djg.Relation.objects.update_or_create(src_id=secondRCR.id, tgt_id=firstRCR.id)

      self.relation_map[model.id] = newRel.id

  def save_inherit(self, model: pyd.Inheritance):
    """
    Saves a inheritance given both classes are already saved in the current run
    """
    djg.Inheritance.objects.update_or_create(parent_id=self.class_map[model.parent.id], child_id=self.class_map[model.child.id])