from rest_framework import serializers

from rex.models.klass import Class, ClassAttributeEnum, ClassAttributePrim, Enum, EnumAttribute, Relation, RelationClassReference

class EnumAttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = EnumAttribute
    exclude = ('polymorphic_ctype',)

class EnumSerializer(serializers.ModelSerializer):
  enum_values = EnumAttributeSerializer(many=True, read_only=True)

  class Meta:
    model = Enum
    exclude = ('polymorphic_ctype',)

class ClassAttributeEnumSerializer(serializers.ModelSerializer):
  enum = EnumSerializer(read_only=True)
  enum_id = serializers.PrimaryKeyRelatedField(
      queryset=Enum.objects.all(),
      source='enum',
      write_only=True
    )
  
  class Meta:
    model = ClassAttributeEnum
    exclude = ('polymorphic_ctype',)

class ClassAttributePrimSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClassAttributePrim
    exclude = ('polymorphic_ctype',)

class ClassSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    fields = ['id', 'name']

class RCRSimpleSerializer(serializers.ModelSerializer):
  ref_class = ClassSimpleSerializer(read_only=True)
  ref_class_id = serializers.PrimaryKeyRelatedField(
    queryset=Class.objects.all(),
    source='ref_class',
    write_only=True
  )

  class Meta:
    model = RelationClassReference
    fields = ['id', 'minim', 'maxim', 'ref_class', 'ref_class_id']

class RelationSerializer(serializers.ModelSerializer):
  src = RCRSimpleSerializer(read_only=True)
  src_id = serializers.PrimaryKeyRelatedField(
    queryset=RelationClassReference.objects.all(),
    source='src',
    write_only=True
  )
  tgt = RCRSimpleSerializer(read_only=True)
  tgt_id = serializers.PrimaryKeyRelatedField(
    queryset=RelationClassReference.objects.all(),
    source='tgt',
    write_only=True
  )

  class Meta:
    model = Relation
    exclude = ('polymorphic_ctype',)

class RelationClassReferenceSerializer(serializers.ModelSerializer):
  rcr_as_src = RelationSerializer(read_only=True)
  rcr_as_tgt = RelationSerializer(read_only=True)

  class Meta:
    model = RelationClassReference
    exclude = ('polymorphic_ctype',)

class ClassSerializer(serializers.ModelSerializer):
  class_primitive_attrs = ClassAttributePrimSerializer(many=True, read_only=True)
  class_enum_attrs = ClassAttributeEnumSerializer(many=True, read_only=True)
  class_relations = RelationClassReferenceSerializer(many=True, read_only=True)

  class Meta:
    model = Class
    exclude = ('polymorphic_ctype',)