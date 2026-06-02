from rest_framework import serializers

from rex.models import klass as cls_mod

class ClassSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = cls_mod.Class
    fields = ['name', 'stereotype']

class ClassAttributeSerializer(serializers.ModelSerializer):
  clazz = ClassSimpleSerializer(read_only=True)
  clazz_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='clazz',
    write_only=True
  )

  class Meta:
    model = cls_mod.ClassAttribute
    exclude = ('polymorphic_ctype',)

class ACRSimpleSerializer(serializers.ModelSerializer):
  class_name = serializers.SerializerMethodField()
  clazz = ClassSimpleSerializer(read_only=True)
  clazz_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='clazz',
    write_only=True
  )

  class Meta:
    model = cls_mod.AssociationClassReference
    fields = ['id', 'class_min', 'class_max', 'clazz', 'clazz_id', 'class_name']

  def get_class_name(self, obj):
    return obj.clazz.name

class AssociationSimpleSerializer(serializers.ModelSerializer):
  src = ACRSimpleSerializer(read_only=True)
  src_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.AssociationClassReference.objects.all(),
    source='src',
    write_only=True
  )
  tgt = ACRSimpleSerializer(read_only=True)
  tgt_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.AssociationClassReference.objects.all(),
    source='tgt',
    write_only=True
  )

  class Meta:
    model = cls_mod.Association
    fields = ['id', 'src', 'src_id', 'tgt', 'tgt_id']

class AssociationSerializer(serializers.ModelSerializer):
  src = ACRSimpleSerializer(read_only=True)
  src_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.AssociationClassReference.objects.all(),
    source='src',
    write_only=True
  )
  tgt = ACRSimpleSerializer(read_only=True)
  tgt_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.AssociationClassReference.objects.all(),
    source='tgt',
    write_only=True
  )

  class Meta:
    model = cls_mod.Association
    exclude = ('polymorphic_ctype',)

class AssociationClassReferenceSerializer(serializers.ModelSerializer):
  class_name = serializers.SerializerMethodField()
  clazz = ClassSimpleSerializer(read_only=True)
  clazz_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='clazz',
    write_only=True
  )
  acr_as_src = AssociationSerializer(read_only=True)
  acr_as_src_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Association.objects.all(),
    source='acr_as_src',
    write_only=True
  )
  acr_as_tgt = AssociationSerializer(read_only=True)
  acr_as_tgt_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Association.objects.all(),
    source='acr_as_tgt',
    write_only=True
  )

  class Meta:
    model = cls_mod.AssociationClassReference
    exclude = ('polymorphic_ctype',)

  def get_class_name(self, obj):
    return obj.clazz.name

class ReadableSerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    if isinstance(instance, cls_mod.ClassAttribute):
      return ClassAttributeSerializer(instance, context=self.context).data

    elif isinstance(instance, cls_mod.Association):
      return AssociationSerializer(instance, context=self.context).data
  
  class Meta:
    model = cls_mod.Readable
    exclude = ('polymorphic_ctype',)

class InheritanceSerializer(serializers.ModelSerializer):
  parent = ClassSimpleSerializer(read_only=True)
  parent_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='parent',
    write_only=True
  )
  child = ClassSimpleSerializer(read_only=True)
  child_id = serializers.PrimaryKeyRelatedField(
    queryset=cls_mod.Class.objects.all(),
    source='child',
    write_only=True
  )

  class Meta:
    model = cls_mod.Inheritance
    exclude = ('polymorphic_ctype',)

class ClassSerializer(serializers.ModelSerializer):
  class_attributes = ClassAttributeSerializer(many=True, read_only=True)
  class_associations = AssociationClassReferenceSerializer(many=True, read_only=True)
  class_parent_in = InheritanceSerializer(many=True, read_only=True)
  class_child_in = InheritanceSerializer(many=True, read_only=True)

  class Meta:
    model = cls_mod.Class
    exclude = ('polymorphic_ctype',)