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

  class Meta:
    model = ClassAttributeEnum
    exclude = ('polymorphic_ctype',)

class ClassAttributePrimSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClassAttributePrim
    exclude = ('polymorphic_ctype',)

class RelationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Relation
    exclude = ('polymorphic_ctype',)

class RelationClassReferenceSerializer(serializers.ModelSerializer):
  rcr_as_srcs = RelationSerializer(many=True, read_only=True)
  rcr_as_tgts = RelationSerializer(many=True, read_only=True)

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