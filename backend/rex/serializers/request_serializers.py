from rest_framework import serializers

class RunAllRequestSerializer(serializers.Serializer):
  input_text = serializers.CharField()