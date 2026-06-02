from ai_gen.models import klass as pyd
from ai_gen.models import ai_klass as aig

class TransformAssociation():
  def transform(associations: list[pyd.Association]) -> list[aig.Association]:
    '''
    pyd.Association.src.class_name
    pyd.Association.src.class_min
    pyd.Association.src.class_max
    pyd.Association.tgt.class_name
    pyd.Association.tgt.class_min
    pyd.Association.tgt.class_max

    aig.Association.src_class_name
    aig.Association.src_class_min
    aig.Association.src_class_max
    aig.Association.tgt_class_name
    aig.Association.tgt_class_min
    aig.Association.tgt_class_max
    '''

    trans_assocs = []

    for assoc in associations:
      trans_assocs.append(aig.Association(
        src_class_name=assoc.src.class_name,
        src_class_min=assoc.src.class_min,
        src_class_max=assoc.src.class_max,
        tgt_class_name=assoc.tgt.class_name,
        tgt_class_min=assoc.tgt.class_min,
        tgt_class_max=assoc.tgt.class_max
      ))
    
    return trans_assocs

  def reverse(associations: list[aig.Association]) -> list[pyd.Association]:
    normal_assoc = []

    for assoc in associations:
      src_acr = pyd.AssociationClassReference(
        class_name=assoc.src_class_name,
        class_min=assoc.src_class_min, class_max=assoc.src_class_max
      )
      tgt_acr = pyd.AssociationClassReference(
        class_name=assoc.tgt_class_name,
        class_min=assoc.tgt_class_min, class_max=assoc.tgt_class_max
      )

      normal_assoc.append(pyd.Association(src=src_acr, tgt=tgt_acr))