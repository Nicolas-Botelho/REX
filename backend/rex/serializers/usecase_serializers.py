from rest_framework import serializers

from rex.models.usecase import Actor, Event, Step, Usecase

class EventSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'name', 'usecase']

class ActorSerializer(serializers.ModelSerializer):
  actor_events = EventSimpleSerializer(many=True, read_only=True)

  class Meta:
    model = Actor
    exclude = ('polymorphic_ctype',)

class StepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Step
    exclude = ('polymorphic_ctype',)

class EventSerializer(serializers.ModelSerializer):
  actor = ActorSerializer(read_only=True)
  actor_id = serializers.PrimaryKeyRelatedField(
    queryset=Actor.objects.all(),
    source='actor',
    write_only=True
  )
  event_steps = StepSerializer(many=True, read_only=True)

  class Meta:
    model = Event
    exclude = ('polymorphic_ctype',)

class UsecaseSerializer(serializers.ModelSerializer):
  usecase_events = EventSerializer(many=True, read_only=True)

  class Meta:
    model = Usecase
    exclude = ('polymorphic_ctype',)