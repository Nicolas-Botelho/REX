from rest_framework.viewsets import ModelViewSet

from rex.models.usecase import Actor, Event, Step, Usecase
from rex.serializers.usecase_serializers import ActorSerializer, EventSerializer, StepSerializer, UsecaseSerializer

class ActorViewSet(ModelViewSet):
  serializer_class = ActorSerializer
  queryset = Actor.objects.all()

class EventViewSet(ModelViewSet):
  serializer_class = EventSerializer
  queryset = Event.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('actor', 'event_steps')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj

class StepViewSet(ModelViewSet):
  serializer_class = StepSerializer
  queryset = Step.objects.all()

class UsecaseViewSet(ModelViewSet):
  serializer_class = UsecaseSerializer
  queryset = Usecase.objects.all()

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())

    if self.action == 'retrieve' or self.action == 'list':
      queryset = queryset.prefetch_related('usecase_events')
    
    obj = get_object_or_404(queryset, **self.kwargs)

    self.check_object_permissions(self.request, obj)
    return obj