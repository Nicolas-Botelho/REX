from typing import List

from ai_gen.models.klass import Enum as Enum_pyd, EnumAttribute as EnumAttr_pyd, Class as Class_pyd, ClassAttributeEnum as ClassAttrEnum_pyd, ClassAttributePrim as ClassAttrPrim_pyd, Relation as Rel_pyd, RelationClassReference as RCR_pyd
from ai_gen.models.response_model.class_response import ClassOutput

from rex.models.klass import Enum as Enum_dj, EnumAttribute as EnumAttr_dj, Class as Class_dj, ClassAttributeEnum as ClassAttrEnum_dj, ClassAttributePrim as ClassAttrPrim_dj, Relation as Rel_dj, RelationClassReference as RCR_dj

class ClassConverter():
  def save(self, classes: ClassOutput):
    for clss in classes.classes:
      Class_dj.objects.create(
        id = clss.ref_id,
        name = clss.name
      )
    for enum in classes.enums:
      Enum_dj.objects.create(
        id = enum.ref_id,
        name = enum.name
      )
    for enumAttr in classes.enum_attributes:
      EnumAttr_dj.objects.create(
        id = enumAttr.ref_id,
        value = enumAttr.value,
        enum_id = enumAttr.enum
      )
    for cae in classes.class_enum_attributes:
      ClassAttrEnum_dj.objects.create(
        id = cae.ref_id,
        name = cae.name,
        enum_id = cae.enum,
        klass_id = cae.klass
      )
    for cap in classes.class_primitive_attributes:
      ClassAttrPrim_dj.objects.create(
        id = cap.ref_id,
        name = cap.name,
        attr_type = cap.attr_type,
        klass_id = cap.klass
      )
    for rcr in classes.relation_class_references:
      RCR_dj.objects.create(
        id = rcr.ref_id,
        minim = rcr.minim,
        maxim = rcr.maxim,
        ref_class_id = rcr.ref_class
      )
    for rel in classes.relations:
      Rel_dj.objects.create(
        id = rel.ref_id,
        src_id = rel.src,
        tgt_id = rel.tgt
      )

  def load(self):
    output = ClassOutput()

    for clss in Class_dj.objects.all():
      cls_pyd = Class_pyd(ref_id=clss.id, name=clss.name)
      output.classes.append(cls_pyd)

      for cap in clss.class_primitive_attrs.all():
        cap_pyd = ClassAttrPrim_pyd(ref_id=cap.id, name=cap.name, attr_type=cap.attr_type, klass=cap.klass_id)
        output.class_primitive_attributes.append(cap_pyd)

      for cae in clss.class_enum_attrs.all():
        cae_pyd = ClassAttrEnum_pyd(ref_id=cae.id, name=cae.name, klass=cae.klass_id, enum=cae.enum.id)
        output.class_enum_attributes.append(cae_pyd)

        enum_pyd = Enum_pyd(ref_id=cae.enum.id, name=cae.enum.name)
        output.enums.append(enum_pyd)

        for e_attr in cae.enum.enum_values.all():
          enumAttr_pyd = EnumAttr_pyd(ref_id=e_attr.id, value=e_attr.value, enum=e_attr.enum_id)
          output.enum_attributes.append(enumAttr_pyd)
      
      for rcr in clss.class_relations.all():
        rcr_pyd = RCR_pyd(ref_id=rcr.id, minim=rcr.minim, maxim=rcr.maxim, ref_class=rcr.ref_class_id)
        output.relation_class_references.append(rcr_pyd)

        for rel in rcr.rcr_as_srcs.all():
          rel_pyd = Rel_pyd(ref_id=rel.id, src=rel.src_id, tgt=rel.tgt_id)
          output.relations.append(rel_pyd)

    return output