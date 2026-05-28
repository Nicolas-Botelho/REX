from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

import rex.models.usecase as uc_mod
import rex.serializers.usecase_serializers as uc_ser

class ActorViewSet(ModelViewSet):
  serializer_class = uc_ser.ActorSerializer
  queryset = uc_mod.Actor.objects.all()

class EventViewSet(ModelViewSet):
  serializer_class = uc_ser.EventSerializer
  queryset = uc_mod.Event.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('actor', 'event_steps')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class StepViewSet(ModelViewSet):
  serializer_class = uc_ser.StepSerializer
  queryset = uc_mod.Step.objects.all()

class ActionViewSet(ModelViewSet):
  serializer_class = uc_ser.ActionSerializer
  queryset = uc_mod.Action.objects.all()

class ModifyActionViewSet(ModelViewSet):
  serializer_class = uc_ser.ModifyActionSerializer
  queryset = uc_mod.ModifyAction.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('class_related_classes')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class ReadActionViewSet(ModelViewSet):
  serializer_class = uc_ser.ReadActionSerializer
  queryset = uc_mod.ReadAction.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('class_related_classes')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj
  
class TextReadActionViewSet(ModelViewSet):
  serializer_class = uc_ser.TextReadActionSerializer
  queryset = uc_mod.TextReadAction.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('class_related_classes')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class DecisionViewSet(ModelViewSet):
  serializer_class = uc_ser.DecisionSerializer
  queryset = uc_mod.Decision.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class UsecaseViewSet(ModelViewSet):
  serializer_class = uc_ser.UsecaseSerializer
  queryset = uc_mod.Usecase.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('usecase_events')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj