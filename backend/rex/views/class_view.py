from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from rex.models import klass as cls_mod
from rex.serializers import class_serializers as cls_ser

class ClassViewSet(ModelViewSet):
  serializer_class = cls_ser.ClassSerializer
  queryset = cls_mod.Class.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('class_attributes', 'class_associations', 'class_parent_in', 'class_child_in')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj
  
class InheritanceViewSet(ModelViewSet):
  serializer_class = cls_ser.InheritanceSerializer
  queryset = cls_mod.Inheritance.objects.all()

class ClassAttributeViewSet(ModelViewSet):
  serializer_class = cls_ser.ClassAttributeSerializer
  queryset = cls_mod.ClassAttribute.objects.all()

class AssociationViewSet(ModelViewSet):
  serializer_class = cls_ser.AssociationSerializer
  queryset = cls_mod.Association.objects.all()

class AssociationClassReferenceViewSet(ModelViewSet):
  serializer_class = cls_ser.AssociationClassReferenceSerializer
  queryset = cls_mod.AssociationClassReference.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.select_related('acr_as_src', 'acr_as_tgt')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj