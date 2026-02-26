from rest_framework import serializers

from rex.models.userstory import UserStory, Epic, Actor

class ActorSerializer(serializers.Serializer):
  class Meta():
    model = Actor
    exclude = ('polymorphic_ctype',)

class UserStorySerializer(serializers.Serializer):
  class Meta():
    model = UserStory
    exclude = ('polymorphic_ctype',)

class EpicSerializer(serializers.Serializer):
  class Meta():
    model = Epic
    exclude = ('polymorphic_ctype',)