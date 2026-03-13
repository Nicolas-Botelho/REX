from rest_framework import serializers

class RunAllResponseSerializer(serializers.Serializer):
  classes = serializers.ListField(child=serializers.DictField(), required=False)
  usecases = serializers.ListField(child=serializers.DictField(), required=False)