from rest_framework.viewsets import ModelViewSet

from rex.models.klass import Class, ClassAttributeEnum, ClassAttributePrim, Enum, EnumAttribute, Relation, RelationClassReference 
from rex.serializers.class_serializers import ClassSerializer, ClassAttributeEnumSerializer, ClassAttributePrimSerializer, EnumSerializer, EnumAttributeSerializer, RelationSerializer, RelationClassReferenceSerializer

class ClassViewSet(ModelViewSet):
  serializer_class = ClassSerializer
  queryset = Class.objects.all()

class ClassAttributeEnumViewSet(ModelViewSet):
  serializer_class = ClassAttributeEnumSerializer
  queryset = ClassAttributeEnum.objects.all()

class ClassAttributePrimViewSet(ModelViewSet):
  serializer_class = ClassAttributePrimSerializer
  queryset = ClassAttributePrim.objects.all()

class EnumViewSet(ModelViewSet):
  serializer_class = EnumSerializer
  queryset = Enum.objects.all()

class EnumAttributeViewSet(ModelViewSet):
  serializer_class = EnumAttributeSerializer
  queryset = EnumAttribute.objects.all()

class RelationViewSet(ModelViewSet):
  serializer_class = RelationSerializer
  queryset = Relation.objects.all()

class RelationClassReferenceViewSet(ModelViewSet):
  serializer_class = RelationClassReferenceSerializer
  queryset = RelationClassReference.objects.all()