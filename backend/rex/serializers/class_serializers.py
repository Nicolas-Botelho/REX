from rest_framework import serializers

from rex.models.klass import Class, ClassAttributeEnum, ClassAttributePrim, Enum, EnumAttribute, Relation, RelationClassReference

class ClassSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    exclude = ('polymorphic_ctype',)

class ClassAttributeEnumSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClassAttributeEnum
    exclude = ('polymorphic_ctype',)

class ClassAttributePrimSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClassAttributePrim
    exclude = ('polymorphic_ctype',)

class EnumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Enum
    exclude = ('polymorphic_ctype',)

class EnumAttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = EnumAttribute
    exclude = ('polymorphic_ctype',)

class RelationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Relation
    exclude = ('polymorphic_ctype',)

class RelationClassReferenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = RelationClassReference
    exclude = ('polymorphic_ctype',)