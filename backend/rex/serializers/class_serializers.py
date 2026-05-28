from rest_framework import serializers

# from rex.models.klass import Class, ClassAttribute, ClassAttributeEnum, ClassAttributePrim, Enum, EnumAttribute, Relation, RelationClassReference, Inheritance
from rex.models import klass as cls_mod

class EnumSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = cls_mod.Enum
    fields = ['id', 'name']

class EnumAttributeSerializer(serializers.ModelSerializer):
  enum = EnumSimpleSerializer(read_only=True)
  enum_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Enum.objects.all(),
    source='enum',
    write_only=True
  )

  class Meta:
    model = cls_mod.EnumAttribute
    exclude = ('polymorphic_ctype',)

class EnumSerializer(serializers.ModelSerializer):
  enum_values = EnumAttributeSerializer(many=True, read_only=True)

  class Meta:
    model = cls_mod.Enum
    exclude = ('polymorphic_ctype',)

class ClassSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = cls_mod.Class
    fields = ['id', 'name']

class ClassAttributeEnumSerializer(serializers.ModelSerializer):
  enum = EnumSerializer(read_only=True)
  enum_id = serializers.PrimaryKeyRelatedField(
      queryset=cls_mod.Enum.objects.all(),
      source='enum',
      write_only=True
    )
  
  class Meta:
    model = cls_mod.ClassAttributeEnum
    exclude = ('polymorphic_ctype',)

class ClassAttributePrimSerializer(serializers.ModelSerializer):
  class Meta:
    model = cls_mod.ClassAttributePrim
    exclude = ('polymorphic_ctype',)

class ClassAttributeSerializer(serializers.ModelSerializer):
  klass = ClassSimpleSerializer(read_only=True)
  klass_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='klass',
    write_only=True
  )

  def to_representation(self, instance):
    if isinstance(instance, cls_mod.ClassAttributePrim):
      return ClassAttributePrimSerializer(instance, context=self.context).data

    elif isinstance(instance, cls_mod.ClassAttributeEnum):
      return ClassAttributeEnumSerializer(instance, context=self.context).data

    return super().to_representation(instance)

  class Meta:
    model = cls_mod.ClassAttribute
    exclude = ('polymorphic_ctype',)

class RCRSimpleSerializer(serializers.ModelSerializer):
  ref_class = ClassSimpleSerializer(read_only=True)
  ref_class_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='ref_class',
    write_only=True
  )

  class Meta:
    model = cls_mod.RelationClassReference
    fields = ['id', 'minim', 'maxim', 'ref_class', 'ref_class_id']

class RelationSimpleSerializer(serializers.ModelSerializer):
  src = RCRSimpleSerializer(read_only=True)
  src_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.RelationClassReference.objects.all(),
    source='src',
    write_only=True
  )
  tgt = RCRSimpleSerializer(read_only=True)
  tgt_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.RelationClassReference.objects.all(),
    source='tgt',
    write_only=True
  )

  class Meta:
    model = cls_mod.Relation
    fields = ['id', 'src', 'src_id', 'tgt', 'tgt_id']

class RelationSerializer(serializers.ModelSerializer):
  src = RCRSimpleSerializer(read_only=True)
  src_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.RelationClassReference.objects.all(),
    source='src',
    write_only=True
  )
  tgt = RCRSimpleSerializer(read_only=True)
  tgt_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.RelationClassReference.objects.all(),
    source='tgt',
    write_only=True
  )

  class Meta:
    model = cls_mod.Relation
    exclude = ('polymorphic_ctype',)

class RelationClassReferenceSerializer(serializers.ModelSerializer):
  rcr_as_src = RelationSerializer(read_only=True)
  rcr_as_tgt = RelationSerializer(read_only=True)
  ref_class = ClassSimpleSerializer(read_only=True)
  ref_class_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='ref_class',
    write_only=True
  )

  class Meta:
    model = cls_mod.RelationClassReference
    exclude = ('polymorphic_ctype',)

class ReadableSerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    if isinstance(instance, cls_mod.ClassAttribute):
      return ClassAttributeSerializer(instance, context=self.context).data

    elif isinstance(instance, cls_mod.Relation):
      return RelationSerializer(instance, context=self.context).data
  
  class Meta:
    model = cls_mod.Readable
    exclude = ('polymorphic_ctype',)

class InheritanceSerializer(serializers.ModelSerializer):
  parent = ClassSimpleSerializer(read_only=True)
  parent_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='parent',
    write_only=True
  )
  child = ClassSimpleSerializer(read_only=True)
  child_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='child',
    write_only=True
  )

  class Meta:
    model = cls_mod.Inheritance
    exclude = ('polymorphic_ctype',)

class ClassSerializer(serializers.ModelSerializer):
  class_attrs = ClassAttributeSerializer(many=True, read_only=True)
  class_relations = RelationClassReferenceSerializer(many=True, read_only=True)
  class_parents = InheritanceSerializer(many=True, read_only=True)
  class_childs = InheritanceSerializer(many=True, read_only=True)

  class Meta:
    model = cls_mod.Class
    exclude = ('polymorphic_ctype',)