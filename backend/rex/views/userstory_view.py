from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from rex.models.userstory import Epic, UserStory, Actor
from rex.serializers.userstory_serializers import EpicSerializer, UserStorySerializer, ActorSerializer

class EpicViewSet(ModelViewSet):
    serializer_class = EpicSerializer
    queryset = Epic.objects.all()

class UserStoryViewSet(ModelViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()

class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()