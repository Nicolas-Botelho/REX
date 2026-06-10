import ai_gen.models.klass as pyd
import rex.models.klass as djg

class ClassSaver():
  def __init__(self):
    self.class_map = {}
    self.attributes_map = {}
    self.association_map = {}
    self.inheritance_map = {}

  def save_model(self, classes: list[pyd.Class], associations: list[pyd.Association], inheritances: list[pyd.Inheritance]):
    for clazz in classes:
      self.save_class(clazz)
    for assoc in associations:
      self.save_assoc(assoc)
    for inher in inheritances:
      self.save_inher(inher)
  
  def save_class(self, clazz: pyd.Class):
    newClass, _ = djg.Class.objects.update_or_create(name=clazz.name, defaults={"stereotype": clazz.stereotype})

    self.class_map[clazz.name] = newClass.id

    for attr in clazz.class_attributes:
      self.save_attr(clazz, attr)

  def save_attr(self, clazz: pyd.Class, attr: pyd.ClassAttribute):
    newAttr, _ = djg.ClassAttribute.objects.update_or_create(name=attr.name, clazz_id=self.class_map[clazz.name], defaults={"attr_type": attr.attr_type, "is_multiple": attr.is_multiple, "valid_values": attr.valid_values})

    self.attributes_map[clazz.name+attr.name] = newAttr.id

  def save_assoc(self, assoc: pyd.Association):
    newSrc = djg.AssociationClassReference.objects.create(clazz_id=self.class_map[assoc.src.class_name], class_min=assoc.src.class_min, class_max=assoc.src.class_max)

    newTgt = djg.AssociationClassReference.objects.create(clazz_id=self.class_map[assoc.tgt.class_name], class_min=assoc.tgt.class_min, class_max=assoc.tgt.class_max)

    newAssoc, _ = djg.Association.objects.update_or_create(src_id=newSrc.id, tgt_id=newTgt.id)

    self.association_map[hash(f"class{newSrc.clazz_id}min{newSrc.class_min}max{newSrc.class_max if newSrc.class_max else "N"}class{newTgt.clazz_id}min{newTgt.class_min}max{newTgt.class_max if newTgt.class_max else "N"}")] = newAssoc.id

  def save_inher(self, inher: pyd.Inheritance):
    newInher, _ = djg.Inheritance.objects.update_or_create(parent_id=self.class_map[inher.parent_class_name], child_id=self.class_map[inher.child_class_name])