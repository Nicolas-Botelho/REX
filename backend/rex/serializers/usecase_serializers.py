from rest_framework import serializers

from rex.models.usecase import Actor, Event, Step, Usecase

class ActorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Actor
    exclude = ('polymorphic_ctype',)

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    exclude = ('polymorphic_ctype',)

class StepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Step
    exclude = ('polymorphic_ctype',)

class UsecaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usecase
    exclude = ('polymorphic_ctype',)