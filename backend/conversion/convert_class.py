from typing import List

from ai_gen.models.klass import Enum as Enum_pyd, EnumAttribute as EnumAttr_pyd, Class as Class_pyd, ClassAttributeEnum as ClassAttrEnum_pyd, ClassAttributePrim as ClassAttrPrim_pyd, Relation as Rel_pyd, RelationClassReference as RCR_pyd
from ai_gen.models.response_model.class_response import ClassOutput

from rex.models.klass import Enum as Enum_dj, EnumAttribute as EnumAttr_dj, Class as Class_dj, ClassAttributeEnum as ClassAttrEnum_dj, ClassAttributePrim as ClassAttrPrim_dj, Relation as Rel_dj, RelationClassReference as RCR_dj

from conversion.utils.case import snake_case

class ClassConverter():
  def save(self, classes: ClassOutput):
    class_map = {}
    enum_map = {}
    rcr_map = {}

    for clss in classes.classes:
      new_cls = Class_dj.objects.create(
        name = clss.name
      )
      class_map[clss.semantic_id] = new_cls.id
    for enum in classes.enums:
      new_enum = Enum_dj.objects.create(
        name = enum.name
      )
      enum_map[enum.semantic_id] = new_enum.id
    for enumAttr in classes.enum_attributes:
      EnumAttr_dj.objects.create(
        value = enumAttr.value,
        enum_id = enum_map[enumAttr.enum]
      )
    for cae in classes.class_enum_attributes:
      ClassAttrEnum_dj.objects.create(
        name = cae.name,
        enum_id = enum_map[cae.enum],
        klass_id = class_map[cae.klass]
      )
    for cap in classes.class_primitive_attributes:
      ClassAttrPrim_dj.objects.create(
        name = cap.name,
        attr_type = cap.attr_type,
        klass_id = class_map[cap.klass]
      )
    for rcr in classes.relation_class_references:
      new_rcr = RCR_dj.objects.create(
        minim = rcr.minim,
        maxim = rcr.maxim,
        ref_class_id = class_map[rcr.ref_class]
      )
      rcr_map[rcr.semantic_id] = new_rcr.id
    for rel in classes.relations:
      Rel_dj.objects.create(
        src_id = rcr_map[rel.src],
        tgt_id = rcr_map[rel.tgt]
      )

  def load(self):
    output = ClassOutput()

    for clss in Class_dj.objects.all():
      snake_class_name = snake_case(clss.name)

      cls_pyd = Class_pyd(semantic_id=snake_class_name, name=clss.name)
      output.classes.append(cls_pyd)

      for cap in clss.class_primitive_attrs.all():
        snake_cap_name = snake_case(cap.name)

        cap_pyd = ClassAttrPrim_pyd(semantic_id=snake_cap_name, name=cap.name, attr_type=cap.attr_type, klass=snake_class_name)
        output.class_primitive_attributes.append(cap_pyd)

      for cae in clss.class_enum_attrs.all():
        snake_cae_name = snake_case(cae.name)
        snake_enum_name = snake_case(cae.enum.name)

        cae_pyd = ClassAttrEnum_pyd(semantic_id=snake_cae_name, name=cae.name, klass=snake_class_name, enum=snake_enum_name)
        output.class_enum_attributes.append(cae_pyd)

        enum_pyd = Enum_pyd(semantic_id=snake_enum_name, name=cae.enum.name)
        output.enums.append(enum_pyd)

        for e_attr in cae.enum.enum_values.all():
          snake_e_attr_name = snake_case(e_attr.value)

          enumAttr_pyd = EnumAttr_pyd(semantic_id=snake_e_attr_name, value=e_attr.value, enum=snake_enum_name)
          output.enum_attributes.append(enumAttr_pyd)
      
      for rcr in clss.class_relations.all():
        snake_rcr_name = f"{snake_class_name}_{rcr.minim if rcr.minim else "n"}-{rcr.maxim if rcr.maxim else "n"}"

        rcr_pyd = RCR_pyd(semantic_id=snake_rcr_name, minim=rcr.minim, maxim=rcr.maxim, ref_class=snake_class_name)
        output.relation_class_references.append(rcr_pyd)

        if hasattr(rcr, "rcr_as_src"):
          snake_tgt_name = f"{rcr.rcr_as_src.tgt.ref_class.name}_{rcr.rcr_as_src.tgt.minim if rcr.rcr_as_src.tgt.minim else "n"}_{rcr.rcr_as_src.tgt.maxim if rcr.rcr_as_src.tgt.maxim else "n"}"

          rel_pyd = Rel_pyd(src=snake_rcr_name, tgt=snake_tgt_name)
          output.relations.append(rel_pyd)

    return output