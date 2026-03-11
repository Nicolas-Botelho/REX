from rest_framework import serializers

class RunAllResponseSerializer(serializers.Serializer):
  items = serializers.DictField()