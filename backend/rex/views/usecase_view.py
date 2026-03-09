from rest_framework.viewsets import ModelViewSet

from rex.models.usecase import Actor, Event, Step, Usecase
from rex.serializers.usecase_serializers import ActorSerializer, EventSerializer, StepSerializer, UsecaseSerializer

class ActorViewSet(ModelViewSet):
  serializer_class = ActorSerializer
  queryset = Actor.objects.all()

class EventViewSet(ModelViewSet):
  serializer_class = EventSerializer
  queryset = Event.objects.all()

class StepViewSet(ModelViewSet):
  serializer_class = StepSerializer
  queryset = Step.objects.all()

class UsecaseViewSet(ModelViewSet):
  serializer_class = UsecaseSerializer
  queryset = Usecase.objects.all()