from typing import List

from ai_gen.models.klass import Enum as enum_pyd, EnumAttribute as enumAttr_pyd, Class as class_pyd, ClassAttributeEnum as classAttrEnum_pyd, ClassAttributePrim as classAttrPrim_pyd, Relation as rel_pyd, RelationClassReference as rcr_pyd
from ai_gen.models.response_model.class_response import ClassOutput

from rex.models.klass import Enum as enum_dj, EnumAttribute as enumAttr_dj, Class as class_dj, ClassAttributeEnum as classAttrEnum_dj, ClassAttributePrim as classAttrPrim_dj, Relation as rel_dj, RelationClassReference as rcr_dj

class ClassConverter():
  def save(self, classes: ClassOutput):
    for clss in classes.classes:
      class_dj.objects.create(
        id = clss.iD,
        name = clss.name
      )
    for enum in classes.enums:
      enum_dj.objects.create(
        id = enum.iD,
        name = enum.name
      )
    for enumAttr in classes.enum_attributes:
      enumAttr_dj.objects.create(
        id = enumAttr.iD,
        value = enumAttr.value,
        enum = enumAttr.enum
      )
    for cae in classes.class_enum_attributes:
      classAttrEnum_dj.objects.create(
        id = cae.iD,
        name = cae.name,
        enum = cae.enum,
        klass = cae.klass
      )
    for cap in classes.class_primitive_attributes:
      classAttrPrim_dj.objects.create(
        id = cap.iD,
        name = cap.name,
        attr_type = cap.attr_type,
        klass = cap.klass
      )
    for rcr in classes.relation_class_references:
      rcr_dj.objects.create(
        id = rcr.iD,
        minim = rcr.minim,
        maxim = rcr.maxim,
        ref_class = rcr.ref_class
      )
    for rel in classes.relations:
      rel_dj.objects.create(
        id = rel.iD,
        src = rel.src,
        tgt = rel.tgt
      )

  def load(self):
    output = ClassOutput()

    for clss in class_dj.objects.all():
      cls_pyd = class_pyd()
      cls_pyd.iD = clss.id
      cls_pyd.name = clss.name

      output.classes.append(cls_pyd)      
      for cap in clss.class_primitive_attrs.all():
        cap_pyd = classAttrPrim_pyd()
        cap_pyd.iD = cap.id
        cap_pyd.name = cap.name
        cap_pyd.attr_type = cap.attr_type
        cap_pyd.klass = cap.klass

        output.class_primitive_attributes.append(cap_pyd)      
      for cae in clss.class_enum_attrs.all():
        cae_pyd = classAttrEnum_pyd()
        cae_pyd.iD = cae.id
        cae_pyd.name = cae.name
        cae_pyd.klass = cae.klass
        cae_pyd.enum = cae.enum.id

        output.class_enum_attributes.append(cae_pyd)

        enu_pyd = enum_pyd()
        enu_pyd.iD = cae.enum.id
        enu_pyd.name = cae.enum.name

        output.enums.append(enu_pyd)
        for e_attr in cae.enum.enum_values.all():
          eAttr_pyd = enumAttr_pyd()
          eAttr_pyd.iD = e_attr.id
          eAttr_pyd.value = e_attr.value
          eAttr_pyd.enum = e_attr.enum

          output.enum_attributes.append(eAttr_pyd)
      
      for rcr in clss.class_relations.all():
        cls_rel_pyd = rcr_pyd()
        cls_rel_pyd.iD = rcr.id
        cls_rel_pyd.minim = rcr.minim
        cls_rel_pyd.maxim = rcr.maxim
        cls_rel_pyd.ref_class = rcr.ref_class

        output.relation_class_references.append(cls_rel_pyd)
        for rel in rcr.rcr_as_srcs.all():
          relat_pyd = rel_pyd()
          relat_pyd.iD = rel.id
          relat_pyd.src = rel.src
          relat_pyd.tgt = rel.tgt

          output.relations.append(relat_pyd)

    return output