from rest_framework import serializers

import rex.models.usecase as uc_mod
import rex.models.klass as cls_mod

import rex.serializers.class_serializers as cls_ser

class EventSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.Event
    fields = ['id', 'name']

class ActorSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.Actor
    exclude = ('polymorphic_ctype',)

class ActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.Action
    exclude = ('polymorphic_ctype',)

# ClassManipulationSerializer to call the ClassSerializer
class ClassManipulationActionSerializer(serializers.ModelSerializer):
  related_classes = cls_ser.ClassSerializer(many=True, read_only=True)
  related_classes_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='related_classes',
    write_only=True
  )

  class Meta:
    model = uc_mod.ClassManipulationAction
    exclude = ('polymorphic_ctype')
    
  def to_representation(self, instance):
    if isinstance(instance, uc_mod.ModifyAction):
      return ModifyActionSerializer(instance, context=self.context).data

    elif isinstance(instance, uc_mod.ReadAction):
      return ReadActionSerializer(instance, context=self.context).data
    
    elif isinstance(instance, uc_mod.TextReadAction):
      return TextReadActionSerializer(instance, context=self.context).data

    return super().to_representation(instance)

class ModifyActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.ModifyAction
    exclude = ('polymorphic_ctype',)

class ReadActionSerializer(serializers.ModelSerializer):
  read_attributes = cls_ser.ReadableSerializer(many=True, read_only=True)
  read_attributes_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Readable.objects.all(),
    source='read_attributes',
    write_only=True
  )

  class Meta:
    model = uc_mod.ReadAction
    exclude = ('polymorphic_ctype',)

class TextReadActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = uc_mod.TextReadAction
    exclude = ('polymorphic_ctype',)

class DecisionSerializer(serializers.ModelSerializer):
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
  first_step = StepSerializer(read_only=True)
  first_step_id = serializers.PrimaryKeyRelatedField(
    queryset=uc_mod.Step.objects.all(),
    source='first_step',
    write_only=True
  )

  class Meta:
    model = uc_mod.Event
    exclude = ('polymorphic_ctype',)

class UsecaseSerializer(serializers.ModelSerializer):
  usecase_events = EventSerializer(many=True, read_only=True)

  class Meta:
    model = uc_mod.Usecase
    exclude = ('polymorphic_ctype',)