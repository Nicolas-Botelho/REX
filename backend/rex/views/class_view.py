from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from rex.models.klass import Class, ClassAttributeEnum, ClassAttributePrim, Enum, EnumAttribute, Relation, RelationClassReference 
from rex.serializers.class_serializers import ClassSerializer, ClassAttributeEnumSerializer, ClassAttributePrimSerializer, EnumSerializer, EnumAttributeSerializer, RelationSerializer, RelationClassReferenceSerializer

class ClassViewSet(ModelViewSet):
  serializer_class = ClassSerializer
  queryset = Class.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('class_primitive_attrs', 'class_enum_attrs', 'class_relations')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class ClassAttributeEnumViewSet(ModelViewSet):
  serializer_class = ClassAttributeEnumSerializer
  queryset = ClassAttributeEnum.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.select_related('enum')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class ClassAttributePrimViewSet(ModelViewSet):
  serializer_class = ClassAttributePrimSerializer
  queryset = ClassAttributePrim.objects.all()

class EnumViewSet(ModelViewSet):
  serializer_class = EnumSerializer
  queryset = Enum.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('enum_values')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class EnumAttributeViewSet(ModelViewSet):
  serializer_class = EnumAttributeSerializer
  queryset = EnumAttribute.objects.all()

class RelationViewSet(ModelViewSet):
  serializer_class = RelationSerializer
  queryset = Relation.objects.all()

class RelationClassReferenceViewSet(ModelViewSet):
  serializer_class = RelationClassReferenceSerializer
  queryset = RelationClassReference.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('rcr_as_srcs', 'rcr_as_tgts')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj