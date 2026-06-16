from rest_framework import serializers

import rex.models.usecase as uc_mod
import rex.models.klass as cls_mod

import rex.serializers.class_serializers as cls_ser

class EventSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.Event
    fields = ['id', 'name']

class StepSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.Step
    fields = ['id', 'step_code', 'description']

class ActorSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.Actor
    exclude = ('polymorphic_ctype',)

class ActionSerializer(serializers.ModelSerializer):
  clazz = cls_ser.ClassSimpleSerializer(read_only=True)
  clazz_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='clazz',
    write_only=True
  )
  event = EventSimpleSerializer(read_only=True)
  event_id = serializers.PrimaryKeyRelatedField(
    queryset=uc_mod.Event.objects.all(),
    source='event',
    write_only=True
  )
  next_step = StepSimpleSerializer(read_only=True)
  next_step_id = serializers.PrimaryKeyRelatedField(
    queryset=uc_mod.Step.objects.all(),
    source='next_step',
    write_only=True
  )

  class Meta:
    model = uc_mod.Action
    exclude = ('polymorphic_ctype',)

class DecisionSerializer(serializers.ModelSerializer):
  clazz = cls_ser.ClassSimpleSerializer(read_only=True)
  clazz_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='clazz',
    write_only=True
  )
  event = EventSimpleSerializer(read_only=True)
  event_id = serializers.PrimaryKeyRelatedField(
    queryset=uc_mod.Event.objects.all(),
    source='event',
    write_only=True
  )
  next_steps = StepSimpleSerializer(read_only=True, many=True)
  next_steps_id = serializers.PrimaryKeyRelatedField(
    queryset=uc_mod.Step.objects.all(),
    source='next_step',
    write_only=True,
    many=True
  )
  
  class Meta:
    model = uc_mod.Decision
    exclude = ('polymorphic_ctype',)

class StepSerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    if isinstance(instance, uc_mod.Action):
      return ActionSerializer(instance, context=self.context).data

    elif isinstance(instance, uc_mod.Decision):
      return DecisionSerializer(instance, context=self.context).data

  class Meta:
    model = uc_mod.Step
    exclude = ('polymorphic_ctype',)

class EventSerializer(serializers.ModelSerializer):
  actor = ActorSerializer(read_only=True)
  actor_id = serializers.PrimaryKeyRelatedField(
    queryset=uc_mod.Actor.objects.all(),
    source='actor',
    write_only=True
  )
  event_steps = StepSerializer(many=True, read_only=True)

  class Meta:
    model = uc_mod.Event
    exclude = ('polymorphic_ctype',)

class UsecaseSerializer(serializers.ModelSerializer):
  usecase_events = EventSerializer(many=True, read_only=True)

  class Meta:
    model = uc_mod.Usecase
    exclude = ('polymorphic_ctype',)